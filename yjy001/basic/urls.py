from django.urls import path
from . import views
urlpatterns=[

        path('', views.fault),
        path('', views.about_us),
        path('', views.about_us2),
        path('', views.blog),
        path('',views.blog_with_sidebar),
        path('', views.checkout),
        path('', views.contact),
        path('', views.courses),
        path('', views.event),
        path('', views.index),
        path('', views.index2),
        path('', views.index3),
        path('', views.index4),
        path('', views.instructor),
        path('', views.login),
        path('', views.login_form),
        path('', views.need_login),
        path('', views.next_register),
        path('', views.register),
        path('', views.register2),
        path('', views.register3),
        path('', views.register_results),
        path('', views.register_results2),
        path('', views.shop),
        path('', views.shop_with_sidebar),
        path('', views.single_blog),
        path('', views.single_courses),
        path('', views.single_event),
        path('', views.single_shop),
        path('', views.update_personalinfo),
        path('', views.view_cart),

                ]
