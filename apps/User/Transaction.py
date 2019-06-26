# -*- coding: utf-8 -*-
 
from apps.User.models import Parent
from apps.course.models import Course_Base
from apps.userHome.models import Temp_Lesson
import datetime

def UpdateInfo(request):
    p=Parent.objects.get(id=1)
    if request.POST.get('PName')!='':
        p.PName=request.POST.get('PName')
                
    if request.POST.get('KName')!='':
        p.KName=request.POST.get('KName')

    if request.POST.get('Age')!='':
        p.Age=request.POST.get('Age')
        
    if request.POST.get('Sex')!='':
        p.Sex=request.POST.get('Sex')

    if request.POST.get('PhoneNumber')!='':
        p.PhoneNumber=request.POST.get('PhoneNumber')

    if request.POST.get('Email')!='':
        p.Email=request.POST.get('Email')

    if request.POST.get('Birthday')!='':
        p.Birthday=request.POST.get('Birthday')

    if request.POST.get('LDirection')!='':
        p.LDirection=request.POST.get('LDirection')

    if request.POST.get('FeeRange')!='':
        p.FeeRange=request.POST.get('FeeRange')

    if request.POST.get('Area')!='':
        p.Area=request.POST.get('Area')

    if request.POST.get('Wallet')!='':
        p.Wallet=request.POST.get('Wallet')

    p.save()

def Recharge(request):
    p=Parent.objects.get(id=1)
    if request.POST.get('Wallet')!='':
       p.Wallet=request.POST.get('Wallet')

    p.save()

def ApplyAudi(request):
    p=Parent.objects.get(id=1)
    c=Course_Base.objects.get(id=1)
    now = datetime.datetime.now()
    if(c.course_time.replace(tzinfo=None)>now):
        tl=Temp_Lesson(person_id=p.id,lesson_id=c.id)
        tl.save()
        return True

    return False

    



        
        
