from django.urls import path
from apps.homepage import views

app_name = 'homepage'

urlpatterns = [
    path(r'HomePage/',views.VisitHomePage),
    path(r'index/',views.VisitIndex),
]
