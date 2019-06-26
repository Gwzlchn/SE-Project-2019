"""yjy001 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('fault/', include('basic.urls')),
    path('about_us/', include('basic.urls')),
    path('about_us2/', include('basic.urls')),
    path('blog/', include('basic.urls')),
    path('blog_with_sidebar/', include('basic.urls')),
    path('checkout/', include('basic.urls')),
    path('contact/', include('basic.urls')),
    path('courses/', include('basic.urls')),
    path('event/', include('basic.urls')),
    path('index/', include('basic.urls')),
    path('index2/', include('basic.urls')),
    path('index3/', include('basic.urls')),
    path('index4/', include('basic.urls')),
    path('instructor/', include('basic.urls')),
    path('login/', include('basic.urls')),
    path('login_form/', include('basic.urls')),
    path('need_login/', include('basic.urls')),
    path('next_register/', include('basic.urls')),
    path('register/', include('basic.urls')),
    path('register2/', include('basic.urls')),
    path('register3/', include('basic.urls')),
    path('register_results/', include('basic.urls')),
    path('register_results2/', include('basic.urls')),
    path('shop/', include('basic.urls')),
    path('shop_with_sidebar/', include('basic.urls')),
    path('single_blog/', include('basic.urls')),
    path('single_courses/', include('basic.urls')),
    path('single_event/', include('basic.urls')),
    path('single_shop/', include('basic.urls')),
    path('update_personalinfo/', include('basic.urls')),
    path('view_cart/', include('basic.urls')),
    path('admin/', admin.site.urls),
    
]
