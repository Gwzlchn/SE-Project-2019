# posts/urls.py
from django.urls import path

from . import views

app_name = 'imageStorage'

urlpatterns = [
    path('postimage/', views.showimage),
    path('postvideo/', views.showvideo)# new
]
