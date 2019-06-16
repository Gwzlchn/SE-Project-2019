# posts/urls.py
from django.urls import path

from . import views

app_name = 'imageStorage'

urlpatterns = [
    path('post/', views.showimage)  # new
]
