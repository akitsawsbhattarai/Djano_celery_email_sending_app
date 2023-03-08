from django.shortcuts import render, HttpResponse
from .tasks import send_mail_task
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
# Create your views here.
from .tasks import send_mail_task
def send_mail(request):
    send_mail_task.delay()
    return HttpResponse("Sent")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=12, minute=18, timezone='Asia/Kathmandu')
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+ "1",task='send_mail_app.tasks.send_mail_task')    
    return HttpResponse("scheduled mail sent")
    