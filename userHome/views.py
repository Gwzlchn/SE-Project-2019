from django.shortcuts import render

# Create your views here.

def TeacherInfo(request):
    return render(request,'userHome\TeacherInfomation.html')
