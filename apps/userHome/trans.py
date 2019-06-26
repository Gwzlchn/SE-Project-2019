from django.contrib.auth.decorators import login_required

import apps.User.models as umodel
from apps.course.models import Course_Base,Course_Institution,Course_Teacher
from apps.fundamental.article.models import Announcement
#@login_required()
def display_Teach_info(id):
    dict = {}
    teacher = umodel.Teacher.objects.get(user_id=id)
    dict['Name'] = teacher.Name
    dict['Age'] = teacher.Age
    dict['Limyear'] = teacher.Limyear
    dict['LDirection'] = teacher.LDirection
    dict['PhoneNumber'] = teacher.PhoneNumber
    dict['Fitage'] = teacher.Fitage
    dict['Sex'] = teacher.Sex
    dict['Wallet'] = teacher.Wallet
    dict['Brief'] = teacher.Brief
    dict['Id_Num'] = teacher.Id_num
    return dict

#@login_required()
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

#@login_required()
def add_course(dict,id):
    course = Course_Base(course_location_province=dict['location_pro'],course_name=dict['name'],
                               course_location_city=dict['location_city'],
                               course_location_area=dict['location_area'],
                               course_teacher=dict['course_teacher'],
                               course_subject=dict['course_subject'],course_price=dict['course_price'],
                               course_age=dict['course_age'],course_time=dict['course_time'],
                               course_contains=dict['course_contains'],course_duration_of_week=dict['course_duration_time'])
    course.save()

    if umodel.Teacher.objects.filter(user_id=id):
        teacher = umodel.Teacher.objects.get(user_id=id)
        Course_Teacher.objects.create(course_teacher=teacher,course_id=course)
    else:
        Course_Institution.objects.create(course_ins=id,course_id=course)
    return

def display_all_course(id,b_id=None):
    dict = {}
    dict['courses'] = []
    if umodel.Teacher.objects.filter(user_id=id):
        teacher = umodel.Teacher.objects.get(user_id=id)
        cc = Course_Teacher.objects.filter(course_teacher=teacher.id)
        i = 0
        for course in cc:
            dict['courses'].append(Course_Base.objects.get(id=course.course_id.id))
    else:
        cc = Course_Institution.objects.filter(course_ins=b_id)
        i = 0
        for course in cc:
            dict['courses'].append(Course_Base.objects.get(id=course.course_id.id))
    return dict

def display_all_ann(id):
    dict = {}
    dict['res'] = []
    anns = Announcement.objects.filter(author_id=id)
    for ann in anns:
        dict['res'].append(ann)
    return dict

def delete_course(c_id,id,b_id=None):
    if not Course_Base.objects.filter(id=c_id):
        if umodel.Teacher.objects.filter(user_id=id):
            teacher = umodel.Teacher.objects.get(user_id=id)
            Course_Teacher.objects.filter(course_id=c_id).filter(course_teacher=teacher.id).delete()
            Course_Base.objects.filter(id=c_id).delete()
        else:
            Course_Institution.objects.filter(course_id=c_id).filter(course_ins=b_id).delete()
            Course_Base.objects.filter(id=c_id).delete()
    return

