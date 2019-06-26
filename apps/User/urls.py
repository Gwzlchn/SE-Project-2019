from django.contrib import admin
from django.urls import path

from apps.User import views

app_name = 'User'

urlpatterns = [
    #path('admin/',admin.site.urls),
    path(r'home/', views.home),
    path(r'register/', views.regChoice),
    path(r'login/', views.Slogin),
    path(r'POSreg/',views.POSreg),
    path(r'Teareg/',views.Teareg),
    path(r'Insreg/',views.Insreg),
    path(r'Admreg/',views.Admreg),
]
