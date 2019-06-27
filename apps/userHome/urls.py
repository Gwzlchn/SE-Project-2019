from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'userHome'

urlpatterns = [
    path(r'',views.dispatch),
    path(r'tChangeInfo',views.change_t_info),
    path(r'SetCourse',views.set_course),
    path(r'tlesson',views.all_tlesson),
    path(r'announcement',views.show_announcement),
    path(r'Addannouncement',views.add_announcement),
    path(r'Updateannouncement',views.update_announcement),
    path(r'AddCourse',views.add_course),
    path('InstitutionInfo/<int:bid>/',views.insinfo),
    path('InstitutionInfo/<int:bid>/ChooseBranch',views.choosebranch),
    path('InstitutionInfo/<int:bid>/AddBranch',views.addbranch)
]