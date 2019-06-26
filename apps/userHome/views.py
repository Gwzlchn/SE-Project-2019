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
    user = request.user
    if Um.Teacher.objects.filter(user_id=user.id):
        return render(request,'userHome/TeacherInfomation.html')
    if Um.Parent.objects.filter(user_id=user.id):
        return render(request,'userHome/ParentInfomation.html')
    if Um.Institution.objects.filter(user_id=user.id):
        return render(request,'userHome/InstitutionInfomation.html')
    if Um.Admin.objects.filter(user_id=user.id):
        return render(request,'userHome/AdminInfomation.html')
#@login_required()
def change_t_info(request):
    id = request.user.id
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
        trans.trans_teach_info(id,dict)
    dict = trans.display_Teach_info(id)
    if request.method == 'POST':
        dict['res'] = 'success!'
    return render(request,'userHome/tChangeInfo.html',dict)

