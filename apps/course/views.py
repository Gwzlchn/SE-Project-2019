from django.shortcuts import render
from .models import Course_Base

# Create your views here.
def Course_Index(request):
    return render(request,"courses.html")

def Single_Course_Index(request,course_id):
    pass
#     print(course_id)
#     course_obj =
#     return render(request,"single_course.html")
