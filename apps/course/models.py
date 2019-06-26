from django.db import models
from ..User.models import Age_Choice,Lesson_Direction,Teacher,Institution,Branch
from apps.fundamental.CHINA_LOCATION.models import ChinaLocation

#假定所有课均是每周一次
class Course_Base(models.Model):

    course_name = models.CharField(max_length=20,verbose_name='课程名称')
    # 课程区域

    course_location_province = models.ForeignKey(ChinaLocation,on_delete=models.CASCADE, \
                                                 related_name='course_province',verbose_name="所在省份")
    course_location_city = models.ForeignKey(ChinaLocation,on_delete=models.CASCADE ,\
                                             related_name='course_city',verbose_name="所在城市")
    course_location_area = models.ForeignKey(ChinaLocation,on_delete=models.CASCADE, \
                                             related_name='course_distinct',verbose_name="所在区")

    course_name=models.CharField(max_length=50,null=False,verbose_name="课程名称")
    course_location_province = models.CharField(max_length=10, null=False, verbose_name="所在省份")
    course_location_city = models.CharField(max_length=20, null=False, verbose_name="所在城市")
    course_location_area = models.CharField(max_length=20, null=False, verbose_name="所在区")


    course_teacher = models.CharField(max_length=30, verbose_name='授课老师')

    course_subject = models.CharField(max_length=10,choices=Lesson_Direction,verbose_name="课程方向")
    course_age = models.CharField(max_length=10,choices=Age_Choice,verbose_name='课程适用年龄')

    course_contains = models.CharField(max_length=500, blank=True, verbose_name="课程内容")

    course_time = models.DateTimeField(verbose_name="首次课时间")

    weeks_choice = [(12,"一季"),(26,"半年"),(52,"一年"),(104,"两年")]
    course_duration_of_week = models.IntegerField(choices=weeks_choice)

    course_price = models.IntegerField(default=0,verbose_name='课程价格')


    # 课程地点
    course_location = models.CharField(max_length=20, default="UNKOWN LOCATION", \
                                       null=False, verbose_name="上课地点")

    course_homework = models.TextField(max_length=500,blank=True,verbose_name='课程作业')


    class Meta:
        db_table = 'Course_Base'



# class Course(models.Model):
#     course_base_id = models.ForeignKey(Course_Base,on_delete=models.CASCADE,null=False)
#
#     # 课程地点
#     course_location = models.CharField(max_length=20, default="UNKOWN LOCATION", \
#                                        null=False, verbose_name="上课地点")
#
#     #本次课时间由首次课时间，一周一节推算出来
#     course_time = models.DateTimeField(verbose_name="本次课时间")
#
#     course_homework = models.TextField(max_length=500,verbose_name='课程作业')
#
#     class Meta:
#         db_table = 'Course'


#
# class Course(models.Model):
#     course_base_id = models.ForeignKey(Course_Base,on_delete=models.CASCADE,null=False)
#
#     # 课程地点
#     course_location = models.CharField(max_length=20, default="UNKOWN LOCATION", \
#                                        null=False, verbose_name="上课地点")
#
#     #本次课时间由首次课时间，一周一节推算出来
#     course_time = models.DateTimeField(verbose_name="本次课时间")
#
#     course_homework = models.TextField(max_length=500,verbose_name='课程作业')
#
#
#     class Meta:
#         db_table = 'Course'
#






# ForeignKey,ManyToManyField与OneToOneField分别在Model中定义多对一，多对多，一对一关系。
class Course_Institution(models.Model):
    course_id = models.ForeignKey(Course_Base,on_delete=models.CASCADE,\
                                  related_name='Course_by_Ins',verbose_name='机构所授课程',null=False)
    course_ins = models.ForeignKey(Branch,on_delete=models.CASCADE,\
                                        related_name='Ins_for_Course',verbose_name='机构名称')

    class Meta:
        db_table = 'Course_Institution'


class Course_Teacher(models.Model):
    course_id = models.ForeignKey(Course_Base,on_delete=models.CASCADE,\
                                  related_name='Course_by_Teacher',verbose_name='教师所授课程')
    course_teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,\
                                        related_name='Teacher_for_course',verbose_name='教师名称')

    class Meta:
        db_table = 'Course_Teacher'

#课程评分
class Course_Score(models.Model):
    course_id = models.ForeignKey(Course_Base,on_delete=models.CASCADE,\
                                  related_name='Course',verbose_name='被评分课程')
    course_score = models.SmallIntegerField(verbose_name='课程评分')
    class Meta:
        db_table = 'Course_Score'





