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
<<<<<<< HEAD
    path(r'POS/',views.POS),
    path(r'Tea/',views.Tea),
    path(r'Adm/',views.Adm),
    path(r'logout/',views.logout),
    path(r'UpdateInfo/', views.VisitUpdateInfo),
    path(r'UResult/', views.VisitUResult),
    path(r'Recharge/', views.VisitRecharge),
    path(r'RResult/', views.VisitRResult),
    path(r'ApplyAudi/',views.VisitApplyAudi),
    path(r'AResult/',views.VisitAResult),
    path(r'Parent/',views.VisitParent),
    #模板url
    path(r'ParentPage/',views.VisitPPage),
    path(r'updatePinfo/',views.VisitUpPInfo),
    path(r'UpPInfo/',views.VisitUpPInfo),
    path(r'UpPInfo-Submit/',views.VisitPPageMB),
    path(r'ParentPageG/',views.VisitPPageG),
    path(r'ParentPageC/',views.VisitPPageC),
    path(r'ParentPageA/',views.VisitPPageA),
    
=======
    path(r'find/',views.Find),
    path(r'logout/',views.logout)
>>>>>>> origin/master
]
