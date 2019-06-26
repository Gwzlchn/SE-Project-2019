from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from . import trans
import apps.User.models as Um
# Create your views here.

def TeacherInfo(request):
    return render(request,'userHome/TeacherInfomation.html')

#@login_required()
def dispatch(request):
    #id = request.user.id
    id = 2
    if Um.Teacher.objects.filter(user_id=id):
        return render(request,'userHome/TeacherInfomation.html')
    if Um.Parent.objects.filter(user_id=id):
        return render(request,'userHome/ParentInfomation.html')
    if Um.Institution.objects.filter(user_id=id):
        return render(request,'userHome/InstitutionInfomation.html')
    if Um.Admin.objects.filter(user_id=id):
        return render(request,'userHome/AdminInfomation.html')
#@login_required()
def change_t_info(request):
    #id = request.user.id
    id = 2
    if not Um.Teacher.objects.filter(user_id=id):
        return render(request,'User/login')
    if request.method == 'POST':
        dict = {}
        dict['Age'] = request.POST.get('Age')
        dict['Limyear'] = request.POST.get('Limyear')
        dict['Fitage'] = request.POST.get('Fitage')
        dict['Brief'] = request.POST.get('Brief')
        dict['PhoneNumber'] = request.POST.get('PhoneNumber')
        dict['LDirection'] = request.POST.get('LDirection')
        trans.change_teach_info(id,dict)
    dict = trans.display_Teach_info(id)
    if request.method == 'POST':
        dict['res'] = 'success!'
    return render(request,'userHome/tChangeInfo.html',dict)

#@login_required()
def set_course(request):
    #id = request.user.id
    id = 2
    if not Um.Teacher.objects.filter(user_id=id):
        return render(request,'User/login')

#@login_required()
def add_course(request):
    #id = request.user.id
    id = 2
    dict = {}
    if not Um.Teacher.objects.filter(user_id=id):
        return render(request,'User/login')
    if request.method == 'POST':
        dict['location_pro'] = request.POST.get('location_pro')
        dict['location_city'] = request.POST.get('location_city')
        dict['location_area'] = request.POST.get('location_area')
        dict['course_teacher'] = request.POST.get('course_teacher')
        dict['course_subject'] = request.POST.get('course_subject')
        dict['course_age'] = request.POST.get('course_age')
        dict['course_contains'] = request.POST.get('course_contains')
        dict['course_time'] = request.POST.get('course_time')
        dict['course_duration_time'] = request.POST.get('course_duration_time')
        dict['course_price'] = request.POST.get('course_price')
        trans.add_course(dict,id)
        dict = {}
        dict['res'] = 'success!'
    return render(request,'userHome/AddCourse.html',dict)

def add_announcement(request):
    return

def update_announcement(request):
    return

def show_announcement(request):
    return

def all_tlesson(request):
    return