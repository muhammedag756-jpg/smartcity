from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .backup import trigger_backup_async



@receiver(post_save, sender="myapp.request_table")
def on_request_saved(sender, instance, created, **kwargs):
    """
    Fires when a user request is created (submitted) or its status is updated
    (pending → assigned → ongoing → completed). Both are worth capturing immediately.
    """
    action = "submitted" if created else f"updated to '{instance.status}'"
    print(f"[SIGNAL] Request {instance.id} {action} → backup queued")
    trigger_backup_async()


# @receiver(post_save, sender="myapp.assign_authority")
# def on_assignment_saved(sender, instance, created, **kwargs):
#     trigger_backup_async()
#
# @receiver(post_delete, sender="myapp.assign_authority")
# def on_assignment_deleted(sender, instance, **kwargs):
#     trigger_backup_async()