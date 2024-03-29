from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'userHome'

urlpatterns = [
    path(r'',views.dispatch),
    path('TeacherInformation',views.TeacherInfo),
    path(r'tChangeInfo',views.change_t_info),
    path(r'SetCourse',views.set_course),
    path(r'tlesson',views.all_tlesson),
    path(r'announcement',views.show_announcement),
    path(r'Addannouncement',views.add_announcement),
    path(r'Updateannouncement',views.update_announcement),
    path(r'AddCourse',views.add_course),
    path('UpdateCourse/<int:cid>/',views.update_course),
    path('InstitutionInfo/<int:bid>/',views.insinfo),
    path('InstitutionInfo/<int:bid>/ChooseBranch',views.choosebranch),
    path('InstitutionInfo/<int:bid>/AddBranch',views.addbranch),
    path('InstitutionInfo/<int:bid>/SetCourse',views.set_course),
    path('InstitutionInfo/<int:bid>/AddCourse',views.add_course),
    path('InstitutionInfo/<int:bid>/InsChangeInfo',views.change_i_info),
    path('InstitutionInfo/<int:bid>/tlesson',views.all_tlesson),
    path('InstitutionInfo/<int:bid>/Addannouncement',views.add_announcement),
    path('InstitutionInfo/<int:bid>/announcement',views.show_announcement),
    path('InstitutionInfo/<int:bid>/Updateannouncement',views.update_announcement),
    path('InstitutionInfo/<int:bid>/UpdateCourse/<int:cid>/',views.update_course),
    path(r'ParentPage/',views.VisitPPage),
    path(r'updatePinfo/',views.VisitUpPInfo),
    path(r'UpPInfo/',views.VisitUpPInfo),
    path(r'UpPInfo-Submit/',views.VisitPPageMB),
    path(r'ParentPageG/',views.VisitPPageG),
    path(r'ParentPageC/',views.VisitPPageC),
    path(r'ParentPageA/',views.VisitPPageA),

]