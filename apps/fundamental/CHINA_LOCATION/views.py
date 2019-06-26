from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import ChinaLocation

# Create your views here.
# 级联菜单
def getAreas(request):
    return render(request,'china_location/location_test.html')

#获得省份
def getProvince(request):
    provinces = ChinaLocation.objects.filter(level=1)
    res = []
    for i in provinces:
        res.append( [i.id , i.name] )
    return JsonResponse({'provinces':res})

#获得城市
def getCity(request):
    city_id = request.GET.get('city_id')
    cities = ChinaLocation.objects.filter(parent_id =city_id)
    res = []
    for i in cities:
        res.append([i.id, i.name])
    return JsonResponse({'cities':res})

#获得区 县
def getDistrict(request):
    district_id = request.GET.get('district_id')
    cities = ChinaLocation.objects.filter(parent_id =district_id)
    res = []
    for i in cities:
        res.append([i.id, i.name])
    return JsonResponse({'district': res})