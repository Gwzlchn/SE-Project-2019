from django.contrib.auth.decorators import login_required

import apps.User.models as umodel
from apps.course.models import Course_Base,Course_Institution,Course_Teacher,Branch
from apps.fundamental.article.models import Announcement
from apps.userHome.models import Temp_Lesson

from django.db.models import Q
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
            course0 = Course_Base.objects.get(id=course.course_id.id)
            temp = [course0,course0.course_location_province.name,course0.course_location_city.name,
                    course0.course_location_distinct.name]
            dict['courses'].append(temp)
    else:
        cc = Course_Institution.objects.filter(course_ins=b_id)
        i = 0
        for course in cc:
            course0 = Course_Base.objects.get(id=course.course_id.id)
            temp = [course0,course0.course_location_province.name,course0.course_location_city.name,
                    course0.course_location_distinct.name]
            dict['courses'].append(temp)

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

def add_ann(dict):
    ann = Announcement(**dict)
    ann.save()
    return

def update_ann(dict):
    ann = Announcement.objects.get(id=dict['id'])
    if ann.title != dict['title']:
        ann.title = dict['title']
    if ann.body != dict['body']:
        ann.body = dict['body']
    ann.save()
    return

def display_all_tlesson(id):
    dict = {}
    dict['res'] = []
    if umodel.Teacher.objects.filter(user_id=id):
        tea = umodel.Teacher.objects.get(user_id=id)
        cts = Course_Teacher.objects.filter(course_id=tea.id)
        for ct in cts:
            tls = Temp_Lesson.objects.filter(lesson=ct.course_id.id).filter(state='待审核')
            for tl in tls:
                dict['res'].append([tl.id,tl.person.PName,tl.lesson.course_name,tl.state])
    else:
        ins = umodel.Institution.objects.get(user_id=id)
        bs = Branch.objects.filter(Ins=ins.id)
        for b in bs:
            lls = Course_Institution.objects.filter(course_ins=b.id)
            for ll in lls:
                course = ll.course_id
                tls = Temp_Lesson.objects.filter(lesson=course.id).filter(state='待审核')
                for tl in tls:
                    dict['res'].append([tl.id,tl.person.Pname,tl.lesson.course_name,tl.state])
    return dict

def deny_tl(id):
    Temp_Lesson.objects.filter(id = id).update(state = '被拒绝')
    return

def allow_tl(id):
    Temp_Lesson.objects.filter(id=id).update(state='已通过')
    return