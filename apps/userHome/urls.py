from django.contrib import admin
from django.urls import path,include
from django import urls
from . import views

app_name = 'userHome'

urlpatterns = [
    path(r'TeacherInfomation/',views.TeacherInfo),
    path(r'userHome/',views.dispatch),
]