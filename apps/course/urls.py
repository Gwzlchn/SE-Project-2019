from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [

    path('index/', views.Course_Index, name='course_index'),
    path('single/',views.Single_Course_Index,name='course_single')

]