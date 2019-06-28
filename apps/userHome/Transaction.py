# -*- coding: utf-8 -*-
 
from apps.User.models import Parent
from apps.course.models import Course_Base
from apps.userHome.models import Temp_Lesson
from apps.sab.models import Pay_Record
import datetime,time

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
       p.Wallet+=float(request.POST.get('Wallet'))

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

    
def ParentPage(request):
    p=Parent.objects.get(id=1)
    rlt={}
    rlt['name']=p.PName
    rlt['money']=p.Wallet
    return rlt


#模块事务
def UpdatePInfo(request):
    p=Parent.objects.get(id=1)
    if request.POST.get('PhoneNumber')!='':
        p.PhoneNumber=request.POST.get('PhoneNumber')

    if request.POST.get('LDirection')!='':
        p.LDirection=request.POST.get('LDirection')

    if request.POST.get('FeeRange')!='':
        p.FeeRange=request.POST.get('FeeRange')

    if request.POST.get('Area')!='':
        p.Area=request.POST.get('Area')


    p.save()




def GetPInfo(request):
    rlt={}
    p=Parent.objects.get(id=1)
    rlt['PName']=p.PName
    rlt['KName']=p.KName
    rlt['Age']=p.Age
    rlt['Sex']=p.Sex
    rlt['PhoneNumber']=p.PhoneNumber
    rlt['LDirection']=p.LDirection
    rlt['FeeRange']=p.FeeRange
    rlt['Area']=p.Area
    rlt['Wallet']=p.Wallet
    return rlt
    
def GetSchedule(request):
    rlt=[]
    p=Parent.objects.get(id=1)
    py=Pay_Record.objects.filter(P_id=p.id)
    for var in py:        
        c=Course_Base.objects.get(id=var.C_id)
        temp={}
        temp['name']=c.course_name
        temp['time']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(c.course_time))
        temp['province']=c.course_location_province.name
        temp['city']=c.course_location_city.name
        temp['distinct']=c.course_location_distinct.name
        temp['location']=c.course_location
        rlt.append(temp)

    return rlt

def GetAudition(request):
    rlt=[]
    p=Parent.objects.get(id=1)
    tl=Temp_Lesson.objects.filter(person_id=p.id)
    for var in tl:        
        c=Course_Base.objects.get(id=var.lesson_id)
        temp={}
        temp['name']=c.course_name
        temp['flag']=var.state
        rlt.append(temp)

    return rlt
