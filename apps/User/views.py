
from django.shortcuts import render,HttpResponse,redirect
from . import Transaction
from apps.User import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import auth
from apps.userHome.views import dispatch
from django.http import HttpResponseRedirect

from functools import wraps

def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwargs):
        if request.session.get('is_login')=='1':
            return f(request,*arg,**kwargs)
        else:
            return redirect('User/login.html')
    return inner

def logout(request):
     request.session['is_login']='0'
     print(request.session['is_login'])
     return render(request,"User/login.html")

def Slogin(request):
    #return HttpResponse("Register")
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            #request.session['is_login']='1'
            #request.session['user_id'] = user.id
            #if user.first_name == "1":"2":"3":"4"
            print('there')
            return HttpResponseRedirect('/userHome/')
        else:
            print('用户名或密码错误!')

    return render(request, "User/login.html", )

def regChoice(request):
    #return HttpResponse("login")
    return render(request, "User/register.html", )

#家长学生注册完毕
def POSreg(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        stuname  = request.POST.get("stuname",None)
        parname  = request.POST.get("parname",None)
        age      = request.POST.get("age",None)
        gender   = request.POST.get("gender",None)
        phone    = request.POST.get("phone",None)
        email    = request.POST.get("email",None)
        #print (username,password,stuname,parname,age,gender)
        #print (phone,email)
        authuser = User.objects.create_user(username,email,password,first_name = '1')
        new_user = models.Parent.objects.create(user = authuser,Age = age)
        new_user.KName = stuname
        new_user.PName = parname
        new_user.Sex = gender
        new_user.PhoneNumber = phone
        new_user.save()
        return render(request, "User/login.html", )  
    return render(request, "User/register3.html", )

def Teareg(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        name     = request.POST.get("name",None)
        id_num   = request.POST.get("id_num",None)
        age      = request.POST.get("age",None)
        gender   = request.POST.get("gender",None)
        Direction= request.POST.get("LDirection",None)
        year     = request.POST.get("Limyear",None)
        Fitage   = request.POST.get("Fitage",None)
        phone    = request.POST.get("phone",None)
        email    = request.POST.get("email",None)
        Brief    = request.POST.get("Brief",None)
        #print(username,password,id_num,name,age,gender)
        #print(Direction,Fitage,phone,email,Brief)
        authuser = User.objects.create_user(username,email,password,first_name = '2')
        new_user = models.Teacher.objects.create(user = authuser)
        new_user.Name = name
        new_user.Age = age
        new_user.Sex = gender
        new_user.Id_num = id_num
        new_user.LDirection = Direction
        new_user.Limyear = year
        new_user.Fitage = Fitage
        new_user.Brief = Brief
        new_user.PhoneNumber = phone
        new_user.save()
        return render(request, "User/login.html", )
    return render(request, "User/register2.html" )
#教育机构注册完毕
def Insreg(request):
    if request.method == "POST":
        iname    = request.POST.get("iname",None)
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        id_num   = request.POST.get("id_num",None)
        address  = request.POST.get("address",None)
        Direction= request.POST.get("LDirection",None)
        Fitage   = request.POST.get("Fitage",None)
        phone    = request.POST.get("phone",None)
        email    = request.POST.get("email",None)
        Brief    = request.POST.get("Brief",None)
        #print(username,password,iname,id_num,address)
        #print(Direction,Fitage,phone,email,Brief)
        
        authuser = User.objects.create_user(username,email,password,first_name = '3')
        new_user = models.Institution.objects.create(user = authuser)
        new_user.Id_num = id_num
        new_user.Address = address
        new_user.LDirection = Direction
        new_user.Fitage = Fitage
        new_user.Brief = Brief
        new_user.PhoneNumber = phone
        new_user.name = iname
        new_user.save()
        
        return render(request, "User/login.html", )
    return render(request,"User/register1.html", )

def Admreg(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        email    = request.POST.get("email",None)
        authuser = User.objects.create_user(username,email,password,first_name = '4')
        new_user = models.Admin.objects.create(user = authuser)
        return render(request, "User/login.html", )
    return render(request,"User/Admreg.html",)


# Create your views here.



def VisitUpdateInfo(request):
    return render(request,"UpdateInfo.html")

def VisitUResult(request):
    Transaction.UpdateInfo(request)
    return render(request,'UResult.html')

def VisitRecharge(request):
    return render(request,'Recharge.html')

def VisitRResult(request):
    Transaction.Recharge(request)
    return render(request,'RResult.html')

def VisitApplyAudi(request):
    return render(request,'ApplyAudi.html')

def VisitAResult(request):
    if Transaction.ApplyAudi(request):
        return render(request,'AResultS.html')


    return render(request,'AResultF.html')

def VisitAddToCart(request):
    return render(request,'AddToCart.html')

def VisitATResult(request):
    Transaction.AddToCart(request)
    return render(request,'ATResult.html')

check_login
def Adm(request):
   Cuid = request.session.get('user_id')
   Utype = User.objects.get(id = Cuid)
   if Utype is not None:
       print(Cuid)
       if(Utype.first_name != '4'):
          return render(request,"User/login.html",)
       print(request.session.get('user_id'))
       return render(request,"User/Adm.html")
   else:
       return render(request,"User/login.html",)

@check_login
def POS(request):
   Cuid = request.session.get('user_id')
   Utype = User.objects.get(id = Cuid)
   if Utype is not None:
       if(Utype.first_name != '1'):
          return render(request,"User/POS.html",)
       print(request.session.get('user_id'))
       return render(request,"User/POS.html")
   else:
       return render(request,"User/login.html",)

@check_login
def Tea(request):
   Cuid = request.session.get('user_id')
   Utype = User.objects.get(id = Cuid)
   if Utype is not None:
       if(Utype.first_name != '2'):
          return render(request,"User/login.html",)
       print(request.session.get('user_id'))
       return render(request,"User/Tea.html")
   else:
       return render(request,"User/login.html",)

