from django.db import models

# Create your models here.
from apps.User.models import Parent
from apps.course.models import Course


class Temp_Lesson(models.Model):
    person = models.ForeignKey(Parent,on_delete=models.CASCADE,verbose_name='试听用户')
    lesson = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='试听课程')
