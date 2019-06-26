from django.db import models
from apps.User.models import Parent
from apps.course.models import Course_Base

# Create your models here.
#购物车
class Shopping_Cart(models.Model):
    Pid = models.ForeignKey(Parent,on_delete=models.CASCADE)
    Cid = models.ForeignKey(Course_Base,on_delete=models.CASCADE)
    Amount = models.IntegerField()

#付款记录
class Pay_Record(models.Model):
    Pid = models.ForeignKey(Parent,on_delete=models.CASCADE)
    CName = models.CharField(max_length=50)
    Amount = models.IntegerField()
    TPrice = models.FloatField()
    Time = models.DateTimeField()

