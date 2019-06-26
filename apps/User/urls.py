from django.contrib import admin
from django.urls import path

from apps.User import views

urlpatterns = [
    #path('admin/',admin.site.urls),
    path('home/', views.home),
    path('register/', views.regChoice),
    path('login/', views.Slogin),
    path('POSreg/',views.POSreg),
    path('Teareg/',views.Teareg),
    path('Insreg/',views.Insreg),
    path('Admreg/',views.Admreg),
]
