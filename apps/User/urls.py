from django.contrib import admin
from django.urls import path

from apps.User import views

app_name = 'User'

urlpatterns = [
    #path('admin/',admin.site.urls),
    path(r'register/', views.regChoice),
    path(r'login/', views.login),
    path(r'login/login-form.html', views.Slogin),
    path(r'register3/',views.POSreg),
    path(r'register2/',views.Teareg),
    path(r'register1/',views.Insreg),
    path(r'Admreg/',views.Admreg),
    path(r'POS/',views.POS),
    path(r'Tea/',views.Tea),
    path(r'Adm/',views.Adm),
    #模板url

    path(r'find/',views.Find),
    path(r'logout/',views.logout)
]
