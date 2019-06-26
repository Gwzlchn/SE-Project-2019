from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [

    path('', views.Course_Index, name='course_index'),
    path('<int:course_id>/' , views.Single_Course_Index,name='course_single')

]