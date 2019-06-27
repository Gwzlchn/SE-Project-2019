from django.contrib import admin
from django.urls import path

from apps.User import views

app_name = 'User'

urlpatterns = [
    #path('admin/',admin.site.urls),
    path(r'register/', views.regChoice),
    path(r'login/', views.Slogin),
    path(r'login/login-form.html',views.realogin),
    path(r'POSreg/',views.POSreg),
    path(r'Teareg/',views.Teareg),
    path(r'Insreg/',views.Insreg),
    path(r'Admreg/',views.Admreg),
    path(r'POS/',views.POS),
    path(r'Tea/',views.Tea),
    path(r'Adm/',views.Adm),
    path(r'logout/',views.logout)
]
