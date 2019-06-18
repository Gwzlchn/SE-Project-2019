from django.db import models
from django.contrib.auth.models import User
# Create your models here.
Gender_Choice=(
    ('M','Male'),
    ('F','Female')
)
Lesson_Direction=(
    ('All','All'),
    ('Chin','Chinese'),
    ('Math','Mathematics'),
    ('Eng','English'),
    ('Phy','Physics'),
    ('Chem','Chemistry'),
    ('Bio','Biology'),
    ('His','History'),
    ('Geo','Geography'),
    ('Poli','Politics')
)
Age_Choice=(
    ('All','All'),
    ('Pri','Primary'),
    ('Jun','Junior'),
    ('Sen','Senior'),
)


class ShoppingCart(models.Model):
    Pid = models.ForeignKey('Parent',on_delete=models.CASCADE)
    Cid = models.ForeignKey('Course',on_delete=models.CASCADE)
    Amount = models.IntegerField()

class PayRecord(models.Model):
    Pid = models.ForeignKey('Parent',on_delete=models.CASCADE)
    CName = models.CharField(max_length=50)
    Amount = models.IntegerField()
    TPrice = models.FloatField()
    Time = models.DateField()

class Parent(models.Model):
    Pid = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='POS')
    PName=models.CharField(max_length=30)
    KName=models.CharField(max_length=30)
    Age=models.IntegerField()
    Sex=models.CharField(max_length=6,choices=Gender_Choice)
    PhoneNumber=models.CharField(max_length=11)
    Birthday = models.DateField()
    LDirection=models.CharField(max_length=15,choices=Lesson_Direction)
    FeeRange=models.IntegerField()
    Area=models.CharField(max_length=10)
    Wallet=models.FloatField(default=0)

class Teacher(models.Model):
    Tid = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='Tea')
    Name = models.CharField(max_length = 32)
    Age  = models.IntegerField(default=0)
    Sex = models.CharField(max_length=6, choices=Gender_Choice)
    Id_num = models.CharField(max_length = 18)
    LDirection = models.CharField(max_length=15,choices=Lesson_Direction)
    Limyear = models.IntegerField(default=0)#从教年限
    Fitage =models.CharField(max_length=15,choices=Age_Choice)
    PhoneNumber = models.CharField(max_length = 20)
    Brief = models.CharField(max_length = 80)
    Wallet=models.FloatField(default=0)

class Institution(models.Model):
    Iid =  models.IntegerField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='Ins')
    Id_num = models.CharField(max_length = 18)
    Address = models.CharField(max_length = 64)
    LDirection = models.CharField(max_length=15,choices=Lesson_Direction)
    Fitage =models.CharField(max_length=15,choices=Age_Choice)
    PhoneNumber = models.CharField(max_length = 20)
    Brief = models.CharField(max_length = 80)
    Wallet=models.FloatField(default=0)



