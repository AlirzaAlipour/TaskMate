from celery import shared_task

@shared_task
def send_task_created_email(user_email, task_title):
    subject = f"New Task Created: {task_title}"
    message = f"A new task has been created for you: {task_title}"
    print(f"Sending email to {user_email}")
    print(f"Subject: {subject}")
    print(f"Message: {message}")