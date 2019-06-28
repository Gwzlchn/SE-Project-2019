# -*- coding: utf-8 -*-
 
from apps.User.models import Parent,Institution,Teacher
from apps.course.models import Course_Base,Course_Institution,Course_Teacher
from apps.sab.models import Shopping_Cart,Pay_Record
import datetime
from django.http import JsonResponse

def AddToCart(request):
    p=Parent.objects.get(id=1)
    c=Course_Base.objects.get(id=1)
    if request.POST.get('Amount')!='':
        sc=Shopping_Cart(P_id=p.id,C_id=c.id,Amount=request.POST.get('Amount'))
        sc.save()


def CheckCart(request):
    CourseList=[]
    p=Parent.objects.get(id=1)
    sc=Shopping_Cart.objects.filter(P_id=p.id)
    if sc!=None:
        CartList=list(sc)
        for var in CartList:
            temp=[]
            c=Course_Base.objects.get(id=var.C_id)
            temp.append(c.course_name)
            temp.append(c.course_price)
            temp.append(var.Amount)
            CourseList.append(temp)

      
    return CourseList

def ResetCart(request):
    p=Parent.objects.get(id=1)
    sc=Shopping_Cart.objects.filter(P_id=p.id)
    if sc!=None:
        for var in sc:
            var.delete()

        return True
    else:
        return False
    

def Pay(request):
    total=0
    p=Parent.objects.get(id=1)
    response=Shopping_Cart.objects.filter(P_id=p.id)
    PayList=list(response)
    for var in PayList:
        total+=Course_Base.objects.get(id=var.C_id).course_price*var.Amount

    if p.Wallet<total:
        return False
    else:
        for var in PayList:
            
            c=Course_Base.objects.get(id=var.C_id)
            SinglePrice=c.course_price*var.Amount
            pr=Pay_Record(P_id=var.P_id,C_id=c.id,CName=c.course_name,Amount=var.Amount,TPrice=SinglePrice,Time=datetime.datetime.now())
            pr.save()
            p.Wallet-=SinglePrice
            p.save()
            ci=Course_Institution.objects.filter(course_id=var.C_id)
            if ci:
                i=Institution.objects.get(id=Course_Institution.objects.get(course_id=var.C_id).course_ins.id)
                i.Wallet+=SinglePrice
                i.save()
            else:
                ct=Course_Teacher.objects.get(course_id=var.C_id)
                t=Teacher.objects.get(id=ct.course_teacher.id)
                t.Wallet+=SinglePrice
                t.save()
                
            var.delete()

        return True  

            
#模块事务
def UpdatePWallet(request):
    p=Parent.objects.get(id=1)
    if request.POST.get('money')!='':
        p.Wallet+=int(request.POST.get('money'))

        p.save()


def GetRecord(request):
    rlt=[]
    p=Parent.objects.get(id=1)
    py=Pay_Record.objects.filter(P_id=p.id)
    for var in py:        
        temp={}
        temp['name']=var.CName
        temp['time']=var.Time.strftime("%Y-%m-%d %H:%M:%S")
        temp['price']=var.TPrice
        temp['amount']=var.Amount
        rlt.append(temp)

    return rlt


def GetCart(request):
    rlt=[]
    p=Parent.objects.get(id=1)
    sc=Shopping_Cart.objects.filter(P_id=p.id)
    for var in sc:        
        c=Course_Base.objects.get(id=var.C_id)
        temp={}
        temp['name']=c.course_name
        temp['price']=c.course_price
        temp['amount']=var.Amount
        temp['total']=c.course_price*var.Amount
        rlt.append(temp)

    return rlt    



        
        
