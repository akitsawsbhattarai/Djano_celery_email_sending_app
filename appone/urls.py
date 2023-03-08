from django.urls import path
from .views import test
app_name = 'appone'
urlpatterns =[
    path('', test, name= "test")
]