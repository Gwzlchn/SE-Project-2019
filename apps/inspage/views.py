from django.shortcuts import render,redirect

from apps.course import models as insmodels
from apps.User import models as usemodels
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import auth
from functools import wraps

# Create your views here.

def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwargs):
        if request.session.get('is_login')=='1':
            return f(request,*arg,**kwargs)
        else:
            return redirect('/login/')
    return inner



def Inst(request):
    Cuid = request.session.get('user_id')
    Utype = User.objects.get(id = Cuid)
    if Utype is  None:
       return render(request,"login.html",)    
       
    Iid = 11 

    if Cuid == Iid:
       print("self")

    inst =  usemodels.Institution.objects.get(user_id = Iid)
    if inst is not None:
       print("Inst_info")
       print(inst.id,inst.Id_num,inst.Address,inst.LDirection,inst.Fitage,inst.PhoneNumber,inst.Wallet)
       print(inst.Brief)
       print("Inst_Comment")
    
    #课程信息模块
    CoF = insmodels.Course_Institution.objects.filter(course_ins = inst.id)
    recorder = []
    num = 1
    print("InstCourseinfo")
    for CofI in CoF:
       print("课程",num,":")
       num +=1
       course = insmodels.Course_Base.objects.get(id = CofI.course_id.id)
       recorder.append(CofI.course_id.id)
       print(course.id,course.course_subject,course.course_age,course.course_teacher)
    
    print(recorder)

    if request.method == 'POST':
       key = request.POST.get("key",None)
       print("looking for",key)
       course_list = insmodels.Course_Base.objects.filter(Q(id__in =  recorder)&Q(course_age = key))
       print("over")
       #复合查询
       for RoS in course_list:
          print(RoS.id)
    
    return render(request,"Ins.html",)