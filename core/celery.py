from __future__ import absolute_import, unicode_literals
import os

from celery import  Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kathmandu')

app.config_from_object(settings, namespace = 'CELERY')

# celery beat settings
app.conf.beat_schedule={
    'send-mail-every-day-at-8':
        {
           'task': 'send_mail_app.tasks.send_mail_task' ,
           'schedule': crontab(hour=11, minute=50, day_of_month=9, day_of_week=4),
           'args':(),
           
        },
}

app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print(f'Request: {self.request!r}')