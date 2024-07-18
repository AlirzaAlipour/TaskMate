from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks.models import Task
from .tasks import send_task_created_email

@receiver(post_save, sender=Task)
def handle_post_save(sender, instance, created, **kwargs):
    if created:
        instance = instance.to_dict()
        user = instance['user']
        title = instance['title']
        send_task_created_email.delay(user, title)
