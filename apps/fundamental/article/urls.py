from . import views
from django.urls import path
app_name = 'article'

urlpatterns = [
    # path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),

    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    #写文章
    path('article-create/', views.article_create, name='article_create'),
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
# 更新文章
    path('article-update/<int:id>/', views.article_update, name='article_update'),
]