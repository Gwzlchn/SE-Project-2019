from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from . import trans
import apps.User.models as Um
from apps.fundamental.article.models import Announcement
from django.http import HttpResponseRedirect
# Create your views here.

def TeacherInfo(request):
    return render(request,'userHome/TeacherInfomation.html')

def dispatch(request):
    print('here')
    id = request.user.id
    print(id)
    if Um.Teacher.objects.filter(user_id=id):
        return render(request,'userHome/TeacherInfomation.html')
    if Um.Parent.objects.filter(user_id=id):
        return render(request,'userHome/ParentInfomation.html')
    if Um.Institution.objects.filter(user_id=id):
        return HttpResponseRedirect('/userHome/InstitutionInfo/0/')
    if Um.Admin.objects.filter(user_id=id):
        return render(request,'userHome/AdminInfomation.html')
    return HttpResponseRedirect('/User/login')

def change_t_info(request):
    id = request.user.id
    if not Um.Teacher.objects.filter(user_id=id):
        return HttpResponseRedirect('/User/login')
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

def set_course(request,bid=None):
    id = request.user.id
    if not Um.Teacher.objects.filter(user_id=id) and not Um.Institution.objects.filter(user_id=id):
        return render(request,'login')
    if bid:
        if request.method == "POST":
            if request.POST.get('delete'):
                c_id = request.POST.get('course_id')
                trans.delete_course(c_id,id,bid)
            else:
                c_id = request.POST.get('id')
                return HttpResponseRedirect('../UpdateCourse'+str(c_id)+'/')
        dict = trans.display_all_course(id,bid)
    else:
        if request.method == "POST":
            c_id = request.POST.get('id')
            trans.delete_course(c_id,id)
        dict = trans.display_all_course(id)
    return render(request,'userHome/SetCourse.html',dict)

def update_course(request,cid,bid=None):
    id = request.user.id
    dict = {}
    if not Um.Teacher.objects.filter(user_id=id) and not Um.Institution.objects.filter(user_id=id):
        return HttpResponseRedirect('/User/login')
    if request.method == 'POST':
        dict['teacher'] = request.POST.get('teacher')
        dict['price'] = request.POST.get('price')
        dict['Address'] = request.POST.get('Address')
        dict['homework'] = request.POST.get('homework')
        trans.update_course(cid,dict)
    dict = trans.display_one_course(cid)
    return render()

def add_course(request,bid=None):
    id = request.user.id
    dict = {}
    if not Um.Teacher.objects.filter(user_id=id) and not Um.Institution.objects.filter(user_id=id):
        return HttpResponseRedirect('/User/login')
    if request.method == 'POST':
        dict['name'] = request.POST.get('name')
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
        trans.add_course(dict,id,bid)
        dict = {}
        dict['res'] = 'success!'
    return render(request,'userHome/AddCourse.html',dict)

def add_announcement(request,bid=None):
    id = request.user.id
    dict = {}
    if not Um.Teacher.objects.filter(user_id=id) and not Um.Institution.objects.filter(user_id=id):
        return HttpResponseRedirect('/User/login')
    if request.method == "POST":
        dict['title'] = request.POST.get('title')
        dict['body'] = request.POST.get('body')
        dict['author'] = request.user
        trans.add_ann(dict)
    return render(request,'userHome/Addannouncement.html',dict)

def update_announcement(request,bid=None):
    id = request.user.id
    if not Um.Teacher.objects.filter(user_id=id) and not Um.Institution.objects.filter(user_id=id):
        return HttpResponseRedirect('/User/login')
    dict = {}
    if request.method == "POST":
        dict['id'] = request.POST.get('id')
        dict['title'] = request.POST.get('title')
        dict['body'] = request.POST.get("body")
        trans.update_ann(dict)
    dict['res'] = '修改成功'
    return render(request,'userHome/Updateannouncement.html',dict)

def show_announcement(request,bid=None):
    id = request.user.id
    if not Um.Teacher.objects.filter(user_id=id) and not Um.Institution.objects.filter(user_id=id):
        return HttpResponseRedirect('/User/login')
    if request.method == "POST":
        aid = request.POST.get('id')
        Announcement.objects.filter(id=aid).delete()
    dict = trans.display_all_ann(id)
    return render(request,'userHome/announcement.html',dict)

def all_tlesson(request,bid = None):
    id = request.user.id
    if not Um.Teacher.objects.filter(user_id=id) and not Um.Institution.objects.filter(user_id=id):
        return HttpResponseRedirect('/User/login')
    if request.method == "POST":
        if request.POST.get('deny'):
            did = request.POST.get('did')
            trans.deny_tl(did)
        else:
            tid = request.POST.get('tid')
            trans.allow_tl(tid)
    dict = trans.display_all_tlesson(id,bid)

    return render(request,'userHome/tlesson.html',dict)

def insinfo(request,bid):
    id = request.user.id
    if not Um.Institution.objects.filter(user_id=id):
        return HttpResponseRedirect('/User/login')
    dict = {}
    dict['bid'] = bid
    return render(request,'userHome/InstitutionInfomation.html',dict)

def choosebranch(request,bid):
    id = request.user.id
    if not Um.Institution.objects.filter(user_id=id):
        return HttpResponseRedirect('/User/login')
    dict={}
    if request.method == 'POST':
        dict['bid'] = request.POST.get('bid')
        print(dict['bid'])
        return HttpResponseRedirect('../'+str(dict['bid'])+'/')
    else:
        dict['bid'] = bid
    return render(request,'userHome/ChooseBranch.html',dict)

def addbranch(request,bid):
    id = request.user.id
    if not Um.Institution.objects.filter(user_id=id):
        return HttpResponseRedirect('/User/login')
    dict={}
    if request.method == 'POST':
        dict['branch_province'] = request.POST.get('branch_province')
        dict['branch_city'] = request.POST.get('branch_city')
        dict['branch_distinct'] = request.POST.get('branch_distinct')
        dict['PhoneNumber'] = request.POST.get('PhoneNumber')
        dict['Address'] = request.POST.get('Address')
        trans.add_branch(dict,id)
        dict['res'] = '添加成功'
    return render(request,'userHome/AddBranch.html',dict)

def change_i_info(request,bid):
    dict = {}
    id = request.user.id
    if not Um.Institution.objects.filter(user_id=id):
        return HttpResponseRedirect('/User/login')
    if request.method == 'POST':
        dict={}
        dict['name'] = request.POST.get('name')
        dict['branch_province'] = request.POST.get('branch_province')
        dict['branch_city'] = request.POST.get('branch_city')
        dict['branch_distinct'] = request.POST.get('branch_distinct')
        dict['Address'] = request.POST.get('Address')
        dict['PhoneNumber'] = request.POST.get('PhoneNumber')
        dict['LDirection'] = request.POST.get('LDirection')
        dict['Fitage'] = request.POST.get('Fitage')
        dict['Brief'] = request.POST.get('Brief')
        trans.change_Ins_info(id,bid,dict)
    dict = trans.display_Ins_info(id,bid)
    if request.method == 'POST':
        dict['res'] = 'success!'
    return render(request,'userHome/InsChangeInfo.html',dict)