from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [

    path('', views.Course_Index, name='course_index'),
    path('<int:course_id>/' , views.Single_Course_Index,name='course_single'),
    path('<int:course_id>/getinfo/',views.Single_Course_Info,name = 'course_info'),

    path('getAllInfo/', views.All_Course_Info, name='All_course_info'),
    path('<int:course_id>/score/' , views.Scoring_Course ,name='course_score'),
    path('<int:course_id>/getcomment/' , views.Single_Course_Comment ,name='course_comment'),

    path('search_course',views.Search_Course,name='search'),
    path('<int:course_id>/comment_submit',views.Comment_Submit,name='submit'),

path('<int:course_id>/add_to_cart',views.Add_To_Cart,name='cart'),
path('<int:course_id>/add_to_temp_lesson',views.Add_To_Temp_Lesson,name='temp_lesson'),

    path('<int:course_id>/comment_del/<int:comment_id>',views.article_delete,name='del'),
]