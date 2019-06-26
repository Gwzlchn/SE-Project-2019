# -*- coding: utf-8 -*-
 
from apps.User.models import Parent,Institution,Teacher
from apps.course.models import Course_Base
from apps.sab.models import Shopping_Cart
import datetime

def AddToCart(request):
    p=Parent.objects.get(id=1)
    c=Course_Base.objects.get(id=1)
    if request.POST.get('Amount')!='':
        sc=Shopping_Cart(person_id=p.id,lesson_id=c.id)
        sc.save()


def Pay(request):
    total=0
    p=Parent.objects.get(id=1)
    response=Shopping_Cart.objects.filter(Pid=p.id)
    PayList=list(response)
    for var in PayList:
        total+=Course_Base.objects.get(id=var.Cid).course_price*var.Amount

    if p.Wallet<total:
        return False
    else:
        for var in PayList:
            var.delete()
            c=Course_Base.objects.get(id=var.Cid)
            pr=PayRecord(Pid=var.Pid,CName=c.course_name,Amount=var.Amount,TPrice=total,Time=datetime.datetime.now)
            pr.save()
            p.Wallet-=total
            p.save()
            ci=Course_Institution.objects.filter(Course_Institution=var.Cid)
            if ci!=None:
                i=Institution.objects.get(id=course_ins)
                i.Wallet+=total
                i.save()
            else:
                ct=Course_Teacher.objects.filter(Course_Teacher=var.Cid)
                t=Teacher.objects.get(id=course_teacher)
                t.Wallet+=total
                t.save()

    

    



        
        
