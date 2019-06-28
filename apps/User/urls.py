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
    
]
