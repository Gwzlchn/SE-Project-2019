from django.db import models
from apps.fundamental.article.models import News
from apps.fundamental.storage.models import Image,Video
from apps.User.models import Institution,Teacher
from apps.course.models import Course_Base

# Create your models here.
#新闻顺序表
class News_Order(models.Model):
    NO=models.ForeignKey(News,on_delete=models.CASCADE)
    Order=models.IntegerField()

class Video_Order(models.Model):
    VO=models.ForeignKey(Video,on_delete=models.CASCADE)
    Order=models.IntegerField()

class Teacher_Order(models.Model):
    TO=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    Order=models.IntegerField()

class Insti_Order(models.Model):
    IO=models.ForeignKey(Institution,on_delete=models.CASCADE)
    Order=models.IntegerField()

class Course_Order(models.Model):
    CO=models.ForeignKey(Course_Base,on_delete=models.CASCADE)
    Order=models.IntegerField()
    
