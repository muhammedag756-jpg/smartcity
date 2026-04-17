import os
import shutil
import subprocess
import sys
import threading
import logging
from datetime import datetime

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

try:
    from apscheduler.schedulers.background import BackgroundScheduler
    SCHEDULER_AVAILABLE = True
except ImportError:
    SCHEDULER_AVAILABLE = False


APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(APP_DIR)

DB_NAME = "smartcity"
MYSQL_CNF = os.path.join(PROJECT_ROOT, "mysql_access.cnf")
CLIENT_SECRETS = os.path.join(PROJECT_ROOT, "client_secrets.json")
CREDS_FILE = os.path.join(PROJECT_ROOT, "mycreds.txt")
MEDIA_DIR = os.path.join(PROJECT_ROOT, "media")

BACKUP_ROOT = os.path.join(PROJECT_ROOT, "backup_local")
BACKUP_DB_DIR = os.path.join(BACKUP_ROOT, "db")
BACKUP_MEDIA_DIR = os.path.join(BACKUP_ROOT, "media")

KEEP_LAST_DB = 3
KEEP_LAST_MEDIA = 2
SIMULATE_DRIVE_FAILURE = False


os.makedirs(BACKUP_DB_DIR, exist_ok=True)
os.makedirs(BACKUP_MEDIA_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("backup")

_drive_instance = None


def _validate_required_paths():
    issues = []
    if not os.path.exists(MYSQL_CNF):
        issues.append(f"MySQL config missing: {MYSQL_CNF}")
    if not os.path.isdir(MEDIA_DIR):
        issues.append(f"Media directory missing: {MEDIA_DIR}")
    return issues


def _get_drive():
    global _drive_instance
    if SIMULATE_DRIVE_FAILURE:
        raise RuntimeError("Drive is set to simulated failure mode for demonstration.")

    if _drive_instance:
        return _drive_instance

    if not os.path.exists(CLIENT_SECRETS):
        raise FileNotFoundError(
            f"Google Drive client secrets file not found: {CLIENT_SECRETS}"
        )

    gauth = GoogleAuth()
    gauth.LoadClientConfigFile(CLIENT_SECRETS)

    if os.path.exists(CREDS_FILE):
        gauth.LoadCredentialsFile(CREDS_FILE)

    if gauth.credentials is None:
        log.info("[DRIVE] First-time login - opening browser...")
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        log.info("[DRIVE] Token expired - refreshing...")
        try:
            gauth.Refresh()
        except Exception:
            gauth.LocalWebserverAuth()
    else:
        gauth.Authorize()

    gauth.SaveCredentialsFile(CREDS_FILE)
    _drive_instance = GoogleDrive(gauth)
    return _drive_instance


def _upload_drive(filepath):
    try:
        drive = _get_drive()
        drive_file = drive.CreateFile({"title": os.path.basename(filepath)})
        drive_file.SetContentFile(filepath)
        drive_file.Upload()
        log.info(f"[DRIVE  OK] Uploaded: {os.path.basename(filepath)}")
        return True
    except Exception as exc:
        log.warning(f"[DRIVE  FAIL] Upload failed: {exc}")
        return False


def _cleanup_drive(prefix, keep_last):
    try:
        drive = _get_drive()
        files = drive.ListFile({"q": "trashed=false"}).GetList()
        matching = [f for f in files if f["title"].startswith(prefix)]
        matching.sort(key=lambda item: item["createdDate"])
        for old_file in matching[:-keep_last]:
            drive.CreateFile({"id": old_file["id"]}).Delete()
            log.info(f"[DRIVE  CLEANUP] Deleted old: {old_file['title']}")
    except Exception as exc:
        log.warning(f"[DRIVE  CLEANUP] Skipped: {exc}")


def _cleanup_local(directory, keep_last):
    files = sorted(
        f for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    )
    for filename in files[:-keep_last]:
        os.remove(os.path.join(directory, filename))
        log.info(f"[LOCAL  CLEANUP] Deleted old: {filename}")


def _upload_with_fallback(filepath, prefix, keep_last, local_dir):
    drive_ok = _upload_drive(filepath)

    if drive_ok:
        log.info("[BACKUP OK] Redundancy active: Local disk + Google Drive")
    else:
        log.warning("[BACKUP INFO] Drive failed - local disk copy preserved as fallback")

    _cleanup_local(local_dir, keep_last)
    _cleanup_drive(prefix, keep_last)


def backup_database():
    filename = f"db_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
    filepath = os.path.join(BACKUP_DB_DIR, filename)

    log.info("[DB] Running mysqldump...")
    try:
        with open(filepath, "w", encoding="utf-8") as out_file:
            result = subprocess.run(
                ["mysqldump", f"--defaults-extra-file={MYSQL_CNF}", DB_NAME],
                stdout=out_file,
                stderr=subprocess.PIPE,
                text=True,
                timeout=60,
            )

        if result.returncode != 0:
            log.error(f"[DB FAIL] mysqldump error: {result.stderr.strip()}")
            if os.path.exists(filepath):
                os.remove(filepath)
            return None

        log.info(f"[DB] Saved locally: {filename}")
        _upload_with_fallback(filepath, "db_", KEEP_LAST_DB, BACKUP_DB_DIR)
        return filepath

    except subprocess.TimeoutExpired:
        log.error("[DB FAIL] mysqldump timed out after 60 seconds")
        return None
    except Exception as exc:
        log.error(f"[DB FAIL] {exc}")
        return None


def backup_media():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_path = os.path.join(BACKUP_MEDIA_DIR, f"media_{timestamp}")
    zip_path = base_path + ".zip"

    log.info("[MEDIA] Zipping media directory...")
    shutil.make_archive(base_path, "zip", MEDIA_DIR)
    log.info(f"[MEDIA] Saved locally: {os.path.basename(zip_path)}")

    _upload_with_fallback(zip_path, "media_", KEEP_LAST_MEDIA, BACKUP_MEDIA_DIR)
    return zip_path


def run_full_backup():
    issues = _validate_required_paths()

    log.info("=" * 50)
    log.info("[BACKUP] Full backup started")

    if issues:
        for issue in issues:
            log.error(f"[CONFIG FAIL] {issue}")
        log.info("[BACKUP] Full backup stopped")
        log.info("=" * 50)
        return False

    db_ok = backup_database() is not None
    media_ok = backup_media() is not None

    if db_ok or media_ok:
        log.info("[BACKUP] Full backup complete")
    else:
        log.error("[BACKUP FAIL] No backup component completed successfully")

    log.info("=" * 50)
    return db_ok or media_ok


def _run_async(fn):
    threading.Thread(target=fn, daemon=True).start()


def trigger_backup_async():
    _run_async(run_full_backup)


def start_daily_scheduler(hour=14, minute=0):
    if not SCHEDULER_AVAILABLE:
        log.warning("[SCHEDULER] apscheduler not installed: pip install apscheduler")
        return None

    scheduler = BackgroundScheduler()
    scheduler.add_job(
        run_full_backup,
        trigger="cron",
        hour=hour,
        minute=minute,
        id="daily_backup",
        replace_existing=True,
        misfire_grace_time=3600,
    )
    scheduler.start()
    log.info(f"[SCHEDULER] Daily backup scheduled at {hour:02d}:{minute:02d}")
    return scheduler


def _print_demo_help():
    print("Backup CLI")
    print("Usage:")
    print("  python myapp/backup.py")
    print("  python myapp/backup.py --simulate-drive-failure")
    print("")
    print("Required project files:")
    print(f"  {MYSQL_CNF}")
    print(f"  {CLIENT_SECRETS}")
    print("")
    print("First run note:")
    print("  Google Drive will open a browser once for OAuth login.")


if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        _print_demo_help()
        sys.exit(0)

    if "--simulate-drive-failure" in sys.argv:
        SIMULATE_DRIVE_FAILURE = True
        log.info("[DEMO] Drive failure simulation is ON")

    success = run_full_backup()
    sys.exit(0 if success else 1)
