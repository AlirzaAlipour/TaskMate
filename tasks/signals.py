from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from emailservice.tasks import send_task_created_email

@receiver(post_save, sender=Task)
def send_email_on_task_creation(sender, instance, created, **kwargs):
    if created:
        send_task_created_email.delay(instance.user.email, instance.title)