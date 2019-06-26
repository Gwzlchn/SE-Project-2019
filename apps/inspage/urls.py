from django.contrib import admin
from django.urls import path

from apps.inspage import views

app_name = 'inspage'

urlpatterns = [
    #path('admin/',admin.site.urls),
    #path('home/', views.home),
    path('',views.Inst),
]
