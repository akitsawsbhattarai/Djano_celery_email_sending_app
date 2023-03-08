from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from core import settings 
# from django.utils import timezone
# from datetime import timedelta

@shared_task(bind = True)
def send_mail_task(self):
    users = get_user_model().objects.all()
    # timezone.localtime(users.date_time) +timedelta(days=2)
    for user in users:
        mail_subject = "CELERY TESTING"
        message = "This is my first attempt to send mail using celery. please wish me a luck! "+ user.email
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message = message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [to_email],
            fail_silently = True
        )
    return "Mail Sent"
