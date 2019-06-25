from django.contrib.auth.decorators import login_required

import apps.User.models as umodel

@login_required()
def display_Teach_info(id):
    dict = {}
    teacher = umodel.Teacher.objects.get(user_id=id)
    dict['Name'] = teacher.name
    dict['Age'] = teacher.Age
    dict['Limyear'] = teacher.Limyear
    dict['LDirection'] = teacher.LDirection
    dict['PhoneNumber'] = teacher.PhoneNumber
    dict['Fitage'] = teacher.Fitage
    dict['Sex'] = teacher.Sex
    dict['Wallet'] = teacher.Wallet
    dict['Brief'] = teacher.Brief
    return dict

@login_required()
def change_teach_info(id,dict):
    teacher = umodel.Teacher.objects.get(user_id = 2)
    tc = umodel.Teacher.objects.filter(id = teacher.id)
    if dict['Age'] != teacher.Age:
        tc.update(Age = dict['Age'])
    if dict['Limyear'] != teacher.Limyear:
        tc.update(Limyear = dict['Limyear'])
    if dict['Fitage'] != teacher.Fitage:
        tc.update(Fitage = dict['Fitage'])
    if dict['Brief'] != teacher.Brief:
        tc.update(Brief = dict['Brief'])
    if dict['PhoneNumber'] != teacher.PhoneNumber:
        tc.update(PhoneNumber = dict['PhoneNumber'])
    if dict['LDirection'] != teacher.LDirection:
        tc.update(LDirection = dict['LDirection'])
    return