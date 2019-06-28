from django.shortcuts import render

# Create your views here.
def VisitHomePage(request):
    return render(request,'HomePage.html')

def VisitIndex(request):
    return render(request,'index.html')
