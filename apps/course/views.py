from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from .models import Course_Base
from apps.fundamental.CHINA_LOCATION.models import ChinaLocation
import json

# Create your views here.
def Course_Index(request):
    return render(request,"courses.html")

def Single_Course_Index(request,course_id):
    return render(request,"single_course.html")

#todo: 时间未处理！！！

def Single_Course_Info(request,course_id):
    course_obj = Course_Base.objects.get(id=course_id)
    dict_obj = course_obj.to_dict()

    dict_obj['province_name'] = ChinaLocation.objects.get(id=dict_obj['course_location_province']).name
    dict_obj['city_name'] = ChinaLocation.objects.get(id=dict_obj['course_location_city']).name
    dict_obj['distinct_name'] = ChinaLocation.objects.get(id=dict_obj['course_location_distinct']).name

    print(dict_obj)
    return JsonResponse(dict_obj)


def All_Course_Info(request):
    course_obj = Course_Base.objects.all()
    dict_obj =[]
    for i in course_obj:
        dict_obj.append( i.to_dict())

    print(dict_obj)
    return JsonResponse({'course_all':dict_obj})

def Scoring_Course(request):
    pass
