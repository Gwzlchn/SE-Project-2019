from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from django.contrib.auth.models import User
import apps.User.models as Um
# Create your views here.

def TeacherInfo(request):
    return render(request,'userHome\TeacherInfomation.html')

@login_required(login_url='User\login')
def dispatch(request):
    user = request.user
    isT = Um.Teach.objects.filter(user_id=user.id)
    isP = Um.POS.objects.filter(user_id=user.id)


