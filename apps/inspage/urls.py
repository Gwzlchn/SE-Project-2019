from django.contrib import admin
from django.urls import path

from apps.inspage import views

app_name = 'inspage'

urlpatterns = [
    #path('admin/',admin.site.urls),
    #path('home/', views.home),
    path(r'inst/<int:iid>',views.Inst),
    path(r'isearch/',views.isearch),
    path(r'tsearch/',views.tsearch),
]
