from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'userHome'

urlpatterns = [
    path(r'',views.dispatch),
    path(r'tChangeInfo',views.change_t_info),
    path(r'SetCourse',views.set_course),
    path(r'tlessons',views.all_tlesson),
    path(r'announcement',views.show_announcement),
    path(r'Addannouncement',views.add_announcement),
    path(r'Updateannouncement',views.update_announcement),

]