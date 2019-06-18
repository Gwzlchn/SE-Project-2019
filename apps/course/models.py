from django.db import models
from ..User.models import  Teach


#假定所有课均是每周一次
class Course_Base(models.Model):
    # course_base_id = models.IntegerField(primary_key=True,serialize=False,verbose_name="课程ID")

    # 课程区域
    course_location_province = models.CharField(max_length=10, null=False, verbose_name="所在省份")
    course_location_city = models.CharField(max_length=20, null=False, verbose_name="所在城市")
    course_location_area = models.CharField(max_length=20, null=False, verbose_name="所在区")
    # 课程地点
    course_location = models.CharField(max_length=20, default="UNKOWN LOCATION",\
                                       null=False, verbose_name="上课地点")
    # 课程老师
    course_teacher = models.ForeignKey(Teach, on_delete=models.CASCADE,\
                                       related_name='Course_Teacher', verbose_name='授课老师')

    course_price = models.IntegerField(max_length=10,default=0,verbose_name='单次课价格')

    course_subject = models.CharField(max_length=10,verbose_name="课程方向")
    course_contains = models.CharField(max_length=500, blank=True, verbose_name="课程内容")


class Course(models.Model):
    # course_id = models.IntegerField(primary_key=True,serialize=False,verbose_name="该次课程ID")
    course_base_id = models.ForeignKey(Course_Base,on_delete=models.CASCADE,verbose_name="大课程ID")

    course_start_time = models.DateTimeField(verbose_name="首次课时间")

    weeks_choice = [(4,"一月"),(12,"一季"),(26,"半年"),(52,"一年"),(104,"两年")]
    course_duration_of_week = models.IntegerField(choices=weeks_choice)

    #课程费用是计算出来的，不储存

    course_homework = models.TextField(max_length=500,verbose_name='课程作业')






