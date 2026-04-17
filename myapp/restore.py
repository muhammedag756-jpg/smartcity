"""
Simple restore script for the academic backup project.

Restore order:
1. Local backup
2. Google Drive backup if local file is missing
"""

import os
import shutil
import subprocess
import sys
import logging

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(APP_DIR)

DB_NAME = "smartcity"
MYSQL_CNF = os.path.join(PROJECT_ROOT, "mysql_access.cnf")
CLIENT_SECRETS = os.path.join(PROJECT_ROOT, "client_secrets.json")
CREDS_FILE = os.path.join(PROJECT_ROOT, "mycreds.txt")
BACKUP_DB_DIR = os.path.join(PROJECT_ROOT, "backup_local", "db")


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("restore")

_drive_cache = None


def _get_drive():
    global _drive_cache
    if _drive_cache:
        return _drive_cache

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
    _drive_cache = GoogleDrive(gauth)
    return _drive_cache


def get_latest_local():
    if not os.path.exists(BACKUP_DB_DIR):
        return None

    files = sorted(
        filename for filename in os.listdir(BACKUP_DB_DIR)
        if filename.endswith(".sql")
    )
    if not files:
        return None

    return os.path.join(BACKUP_DB_DIR, files[-1])


def download_latest_from_drive():
    try:
        log.info("[DRIVE] Connecting to Google Drive...")
        drive = _get_drive()
        files = drive.ListFile({"q": "trashed=false"}).GetList()
        db_files = [
            item for item in files
            if item["title"].startswith("db_") and item["title"].endswith(".sql")
        ]

        if not db_files:
            log.error("[DRIVE FAIL] No DB backup file found on Drive")
            return None

        db_files.sort(key=lambda item: item["createdDate"], reverse=True)
        latest = db_files[0]

        os.makedirs(BACKUP_DB_DIR, exist_ok=True)
        destination = os.path.join(BACKUP_DB_DIR, latest["title"])

        log.info(f"[DRIVE] Downloading latest DB backup: {latest['title']}")
        drive_file = drive.CreateFile({"id": latest["id"]})
        drive_file.GetContentFile(destination)
        log.info(f"[DRIVE OK] Downloaded to: {destination}")
        return destination

    except Exception as exc:
        log.error(f"[DRIVE FAIL] Download failed: {exc}")
        return None


def restore_db(sql_path):
    if not os.path.exists(MYSQL_CNF):
        log.error(f"[RESTORE FAIL] MySQL config missing: {MYSQL_CNF}")
        return False

    log.info(f"[RESTORE] Restoring DB from: {os.path.basename(sql_path)}")
    try:
        with open(sql_path, "r", encoding="utf-8", errors="ignore") as sql_file:
            result = subprocess.run(
                ["mysql", f"--defaults-extra-file={MYSQL_CNF}", DB_NAME],
                stdin=sql_file,
                stderr=subprocess.PIPE,
                text=True,
                timeout=60,
            )

        if result.returncode == 0:
            log.info(f"[RESTORE OK] Database '{DB_NAME}' restored successfully")
            return True

        log.error(f"[RESTORE FAIL] MySQL error: {result.stderr.strip()}")
        return False

    except subprocess.TimeoutExpired:
        log.error("[RESTORE FAIL] Restore timed out after 60 seconds")
        return False
    except Exception as exc:
        log.error(f"[RESTORE FAIL] {exc}")
        return False


def run_restore(force_source="auto"):
    log.info("=" * 52)
    log.info("[RESTORE] Starting restore process")
    log.info(f"[RESTORE] Source mode: {force_source}")
    log.info("=" * 52)

    sql_path = None
    source_used = None

    if force_source in ("auto", "local"):
        local_path = get_latest_local()
        if local_path:
            sql_path = local_path
            source_used = "local"
            log.info(f"[LOCAL OK] Using local backup: {os.path.basename(local_path)}")
        else:
            log.warning("[LOCAL FAIL] No local backup found")
            if force_source == "local":
                return False

    if sql_path is None or force_source == "drive":
        log.info("[FAILOVER] Trying Google Drive backup")
        drive_path = download_latest_from_drive()
        if drive_path:
            sql_path = drive_path
            source_used = "drive"
        else:
            log.error("[RESTORE FAIL] Both local and Drive sources are unavailable")
            return False

    log.info(
        f"[RESTORE] Final source selected: {source_used.upper()} - {os.path.basename(sql_path)}"
    )
    return restore_db(sql_path)


def run_demo():
    print("\n====================================================")
    print("DEMO: Restore failover from Local to Google Drive")
    print("====================================================\n")

    print("Step 1: Ensure at least one DB backup exists.")
    print("Run: python myapp/backup.py")
    input("\nPress Enter after the backup is ready...")

    print("\nStep 2: Simulate local failure by removing local DB backup files.")
    if os.path.exists(BACKUP_DB_DIR):
        shutil.rmtree(BACKUP_DB_DIR)
    os.makedirs(BACKUP_DB_DIR, exist_ok=True)
    print(f"Local DB backup folder cleared: {BACKUP_DB_DIR}")
    input("\nPress Enter to start restore...")

    print("\nStep 3: Auto restore will now fail over to Google Drive.")
    success = run_restore("auto")

    print("\n====================================================")
    if success:
        print("RESULT: Restore successful using failover.")
    else:
        print("RESULT: Restore failed. Check MySQL and Google Drive settings.")
    print("====================================================\n")


if __name__ == "__main__":
    if "--demo" in sys.argv:
        run_demo()
        sys.exit(0)

    if "--source" in sys.argv:
        index = sys.argv.index("--source")
        source = sys.argv[index + 1] if index + 1 < len(sys.argv) else "auto"
        success = run_restore(source)
        sys.exit(0 if success else 1)

    success = run_restore("auto")
    sys.exit(0 if success else 1)
