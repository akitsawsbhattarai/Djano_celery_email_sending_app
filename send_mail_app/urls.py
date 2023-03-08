from django.urls import path, include
from .views import send_mail, schedule_mail
app_name = 'sendmail'
urlpatterns = [
    path('mail/', send_mail, name='sent'),
    path('schedulemail/', schedule_mail, name='schedulemail'),
]
