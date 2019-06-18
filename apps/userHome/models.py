from django.db import models

# Create your models here.
from apps.User.models import POS
from apps.course.models import Course
class tlesson(models.Model):
    person = models.ForeignKey(POS,on_delete=models.CASCADE,verbose_name='试听用户')
    lesson = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='视听课程')
