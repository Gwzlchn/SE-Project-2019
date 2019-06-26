from django.db import models

# Create your models here.
from apps.User.models import Parent
from apps.course.models import Course_Base
class Temp_Lesson(models.Model):
    person = models.ForeignKey(Parent,on_delete=models.CASCADE,verbose_name='试听用户')
    lesson = models.ForeignKey(Course_Base,on_delete=models.CASCADE,verbose_name='视听课程')
