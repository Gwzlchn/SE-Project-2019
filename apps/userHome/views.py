from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from . import trans
import apps.User.models as Um
# Create your views here.

def TeacherInfo(request):
    return render(request,'userHome/TeacherInfomation.html')

@login_required(login_url='User/login')
def dispatch(request):
    user = request.user
    isT = Um.Teach.objects.filter(user_id=user.id)
    isP = Um.POS.objects.filter(user_id=user.id)

@login_required(login_url='User/login')
def change_t_info(request):
    id = request.user.id
    if not Um.Teacher.objects.filter(user_id=id):
        return render(request,'User/login')
    if request.method == 'POST':
        dict = {}
        dict['Age'] = request.POST.get('Age')
        dict[''] = request.POST.get('Age')
        dict['Age'] = request.POST.get('Age')
        dict['Age'] = request.POST.get('Age')
        dict['Age'] = request.POST.get('Age')
        trans.trans_teach_info()
    dict = trans.display_Teach_info(user)
    return render(request,'userHome/tChangeInfo.html',dict)

