from django.shortcuts import render,redirect

from apps.course import models as insmodels
from apps.User import models as usemodels
from apps.fundamental.comment import models as fmodels
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import auth
from functools import wraps

# Create your views here.

def Inst(request,iid = None):
    Iid = iid
    try:
       inst =  usemodels.Institution.objects.get(id = Iid)
    except usemodels.Institution.DoesNotExist:
       inst = None
    if inst is not None:
       #课程信息模块
       CofI = insmodels.Course_Institution.objects.filter(course_ins = inst.id)
       cosl = []
       for Cof in CofI:
           course = insmodels.Course_Base.objects.get(id = Cof.course_id.id)
           cosl.append(course)
       #机构评论
       '''
       ComI = insmodels.Comment_Ins.objects.filter(com_ins = inst.id)
       coml = []
       for Com in ComI:
           com = fmodels.Commenr_Ins.objects.get(id = Com.course_id.id)
       '''   
       res = {"inst":inst,"cou":cosl}
       return render(request,"ins/Ins.html",{'data':res})
    return render(request,"ins/Ins.html",)

def isearch(request):
    if request.method == "POST":
        age = request.POST.get('Fitage',None)
        ld = request.POST.get('LDirection',None)
        print(age,ld)
        if age is not None and age != 'All':
           if ld is not None and ld != 'All':
                relist = usemodels.Institution.objects.filter(Q(Fitage = age)&Q(LDirection = ld))
           else:
                relist = usemodels.Institution.objects.filter(Fitage = age)
        else:
           if ld is not None and ld != 'All':
                relist = usemodels.Institution.objects.filter(LDirection = ld)
           else:
                relist = usemodels.Institution.objects.all()
        wanted = []
        for re in relist:
            print(re)
            wanted.append(re)
        return render(request,"ins/ires.html",{'data':wanted})
    return render(request,"ins/isearch.html",)

def tsearch(request):
    if request.method == "POST":
        age = request.POST.get('Fitage',None)
        ld = request.POST.get('LDirection',None)
        print(age,ld)
        if age is not None and age != 'All':
             if ld is not None and ld != 'All':
                relist = usemodels.Teacher.objects.filter(Q(Fitage = age)&Q(LDirection = ld))
             else:
                relist = usemodels.Teacher.objects.filter(Fitage = age)
        else:
             if ld is not None and ld != 'All':
                relist = usemodels.Teacher.objects.filter(LDirection = ld)
             else:
                relist = usemodels.Teacher.objects.all()

        wanted = []
        for re in relist:
            print(re)
            wanted.append(re)
        return render(request,"ins/tres.html",{'data':wanted})
    return render(request,"ins/tsearch.html",)
