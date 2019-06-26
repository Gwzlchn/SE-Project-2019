from django.shortcuts import render

# Create your views here.
def Course_Index(request):
    return render(request,"courses.html")

def Single_Course_Index(request):
    return render(request,"single_course.html")
