from django.db import models
from django.contrib.auth.models import User
from apps.fundamental.CHINA_LOCATION.models import ChinaLocation
# Create your models here.


Gender_Choice=(
    ('Male','M'),
    ('Female','F')
)
Lesson_Direction=(
    ('All','All'),
    ('Chinese','Chin'),
    ('Mathematics','Math'),
    ('English','Eng'),
    ('Physics','Phy'),
    ('Chemistry','Chem'),
    ('Biology','Bio'),
    ('History','His'),
    ('Geography','Geo'),
    ('Politics','Poli')
)
Age_Choice=(
    ('All','All'),
    ('Primary','Pri'),
    ('Junior','Jun'),
    ('Senior','Sen'),
)

class Parent(models.Model):
    #Pid = models.IntegerField(primary_key=True)
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
    #Tid = models.IntegerField(primary_key=True)
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
    #Iid =  models.IntegerField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='Ins')
    Id_num = models.CharField(max_length = 18)
    LDirection = models.CharField(max_length=15,choices=Lesson_Direction)
    Fitage =models.CharField(max_length=15,choices=Age_Choice)
    PhoneNumber = models.CharField(max_length = 20)
    Brief = models.CharField(max_length = 80)
    Wallet=models.FloatField(default=0)
    name = models.CharField(max_length=30,default='待填写')

class Branch(models.Model):
    Ins = models.ForeignKey(Institution,on_delete=models.CASCADE)
    branch_province = models.ForeignKey(ChinaLocation,on_delete=models.CASCADE, \
                                                 related_name='branch_province',verbose_name="所在省份")
    branch_city = models.ForeignKey(ChinaLocation,on_delete=models.CASCADE , \
                                             related_name='branch_city',verbose_name="所在城市")
    branch_distinct = models.ForeignKey(ChinaLocation,on_delete=models.CASCADE, \
                                                 related_name='branch_distinct',verbose_name="所在区")
    Address = models.CharField(max_length=50,default=None)
    LDirection = models.CharField(max_length=15,choices=Lesson_Direction)
    Fitage =models.CharField(max_length=15,choices=Age_Choice)
    PhoneNumber = models.CharField(max_length = 20)

class Admin(models.Model):
    Aid =  models.IntegerField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='Adm')

