from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Course_Base

# Create your views here.
def Course_Index(request):
    return render(request,"courses.html")

def Single_Course_Index(request,course_id):
    return render(request,"single_course.html")

def Single_Course_Teacher(request,course_id):

    return JsonResponse({'Teacher':'my_teacher_name'})

def Scoring_Course(request):
    pass
