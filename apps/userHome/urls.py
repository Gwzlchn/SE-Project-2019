from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'userHome'

urlpatterns = [
    path(r'userHome/',views.dispatch),
    path(r'tChangeInfo',views.change_t_info),

]