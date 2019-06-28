from django.shortcuts import render
from django.http import HttpResponse
from apps.sab import Transaction

# Create your views here.
def VisitAddToCart(request):
    return render(request,'AddToCart.html')

def VisitATResult(request):
    Transaction.AddToCart(request)
    return render(request,'ATResult.html')

def VisitResetCart(request):
    Transaction.ResetCart(request)
    print('Successful!')
    return render(request,'AddToCart.html')

def VisitCheckCart(request):
    return render(request,'CheckCart.html')

def VisitCheckResult(request):
    return render(request,'CheckResult.html',{'data':Transaction.CheckCart(request)})

def VisitPay(request):
    flag=Transaction.Pay(request)
    if flag==False:
        return HttpResponse('Fail!')
    else:
        return HttpResponse('Success!')

#模板views
def Visitvc(request):
    return render(request,'view-cart.html')

def VisitPRecharge(request):
    return render(request,'PRecharge.html')

def ReturnPPage(request):
    Transaction.UpdatePWallet(request)
    return render(request,'ParentPage.html')

def VisitPPageR(request):
    rlt={}
    rlt['data']=Transaction.GetRecord(request)
    #print(rlt)
    return render(request,'ParentPageR.html',rlt)

def VisitCart(request):
    rlt={}
    rlt['data']=Transaction.GetCart(request)
    return render(request,'view-cart.html',rlt)


def ResetCart(request):
    Transaction.ResetCart(request)
    return VisitCart(request)

def PayForCart(request):
    Transaction.Pay(request)
    return VisitCart(request)
    
