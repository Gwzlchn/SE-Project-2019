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


def getAll(request):
    province_id =  request.GET.get('province_id')
    city_id = request.GET.get('city_id')
    district_id = request.GET.get('district_id')

    province_name = ChinaLocation.objects.get(id= province_id).name
    city_name = ChinaLocation.objects.get(id=city_id).name
    district_name = ChinaLocation.objects.get(id= district_id).name
    res = {province_id:province_name,city_id:city_name,district_id:district_name}
    print(res)
    return JsonResponse(res,safe=False)

