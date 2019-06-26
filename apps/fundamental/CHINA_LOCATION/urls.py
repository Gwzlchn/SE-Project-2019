from django.urls import path
from . import views

app_name = 'CHINA_LOCATION'

urlpatterns = [

    path('test/', views.getAreas, name='loc_test'),
    path('getProvince/',views.getProvince,name='loc_province'),
    path('getCity/',views.getCity,name='loc_city'),
    path('getDistrict/',views.getDistrict,name='loc_distinct'),
]