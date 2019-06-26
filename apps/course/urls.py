from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [

    path('', views.Course_Index, name='course_index'),
    path('<int:course_id>/' , views.Single_Course_Index,name='course_single'),
    path('<int:course_id>/getinfo/',views.Single_Course_Teacher,name = 'course_info'),
    path('<int:course_id>score/' , views.Scoring_Course ,name='course_score'),
]