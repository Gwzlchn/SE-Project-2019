"""SE URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from apps.User import views
import apps.userHome.views as ahv


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'userHome/',include('apps.userHome.urls', namespace='userHome')),
    path('User/',include('apps.User.urls',namespace='User')),
    path('article/', include('apps.fundamental.article.urls', namespace='article')),
    path('ins/',include('apps.inspage.urls',namespace='inspage')),
    path('UpdateInfo/', views.VisitUpdateInfo),
    path('UResult/', views.VisitUResult),
    path('Recharge/', views.VisitRecharge),
    path('RResult/', views.VisitRResult),
    path('ApplyAudi/',views.VisitApplyAudi),
    path('AResult/',views.VisitAResult),
    path('AddToCart/',views.VisitAddToCart),
    path('ATResult/',views.VisitATResult),
    #测试用
    path('storage/', include('apps.fundamental.storage.urls', namespace='storage')),
    path('comment/', include('apps.fundamental.comment.urls', namespace='comment')),

    path('loc/',    include('apps.fundamental.CHINA_LOCATION.urls',namespace='CHINA_LOCATION')),

    path('course/', include('apps.course.urls', namespace='Course')),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
