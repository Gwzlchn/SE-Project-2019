from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.core import serializers
from django.forms.models import model_to_dict
from .models import Course_Base,Course_Comment,Parent
from apps.fundamental.CHINA_LOCATION.models import ChinaLocation
from apps.sab.models import Shopping_Cart
from apps.userHome.models import Temp_Lesson
import json
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def Course_Index(request):
    return render(request,"courses.html")

def Single_Course_Index(request,course_id):
    return render(request,"single_course.html")

def Search_Course(request):
    print(request)
    province_id =  request.GET.get('province_id')
    city_id = request.GET.get('city_id')
    district_id = request.GET.get('district_id')
    course_obj = Course_Base.objects.filter(course_location_province_id=province_id,
                                            course_location_city_id=city_id,
                                            course_location_distinct_id = district_id)


    dict_obj = []
    for i in course_obj:
        dict_obj.append(i.to_dict())

    print(dict_obj)
    print(dict_obj)

    return render(request,"search_courses.html",{'course_all': dict_obj})



#todo: 时间未处理！！！

def Single_Course_Info(request,course_id):
    course_obj = Course_Base.objects.get(id=course_id)
    dict_obj = course_obj.to_dict()

    dict_obj['province_name'] = ChinaLocation.objects.get(id=dict_obj['course_location_province']).name
    dict_obj['city_name'] = ChinaLocation.objects.get(id=dict_obj['course_location_city']).name
    dict_obj['distinct_name'] = ChinaLocation.objects.get(id=dict_obj['course_location_distinct']).name

    #print(dict_obj)
    return JsonResponse(dict_obj)


def All_Course_Info(request):
    course_obj = Course_Base.objects.all()
    dict_obj =[]
    for i in course_obj:
        dict_obj.append( i.to_dict())
    return JsonResponse({'course_all':dict_obj})










def Scoring_Course(request):
    pass


def Single_Course_Comment(request,course_id):
    comment_set = Course_Comment.objects.filter(course_id=course_id)
    dict_obj = []
    for i in comment_set:
        i_dict_temp = i.to_dict()
        #print(i.comment_parent)
        i_dict_temp['Parent_Name'] = i.comment_parent.PName
        #print(i_dict_temp)
        dict_obj.append(i_dict_temp)

    return JsonResponse({'comment': dict_obj})


def Comment_Submit(request,course_id):
    print(request)
    user_id = request.user.id
    comment = request.GET['comment_text']
    print(user_id)
    print(comment)
    res= {'uid':user_id,'comment_text':comment}
    return render(request,"single_course.html",res)

def Add_To_Cart(request,course_id):

    uid= request.user.id
    cid = course_id
    amount = Course_Base.objects.get(id=course_id).course_price
    if uid is not None and cid is not None:
        cart = Shopping_Cart()
        cart.Amount = amount
        cart.C_id = cid
        cart.P_id = uid
        cart.save()

    return redirect(reverse('course:course_single', kwargs={'course_id':course_id}))


def Add_To_Temp_Lesson(request,course_id):
    uid = request.user.id
    cid = course_id
    obj = Temp_Lesson.objects.filter(person_id=uid,lesson_id=course_id)
    if uid is not None and cid is not None and obj is None:
        tl = Temp_Lesson()
        tl.person_id = uid
        tl.lesson_id = cid
        tl.save()
        
    return redirect(reverse('course:course_single', kwargs={'course_id':course_id}))