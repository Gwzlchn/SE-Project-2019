from django.contrib.auth.decorators import login_required

import apps.User.models as umodel

@login_required(login_url='User\login')
def display_Teach_info(user):
    dict = {}
    teacher = umodel.Teach.objects.get(t_user=user.id)
    dict['name'] = teacher.name
    return dict
