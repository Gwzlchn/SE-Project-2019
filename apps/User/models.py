from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

GENDER_CHOICES = ( ('male', "男"),('female', "女"))


class POS(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='extension')
    name = models.CharField(max_length = 32, verbose_name="姓名")
    pname = models.CharField(max_length = 32, verbose_name="家长姓名")
    age  = models.IntegerField(default=0, verbose_name="年龄")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name="性别")
    email = models.EmailField(verbose_name="邮箱")
    phone = models.CharField(max_length = 20, verbose_name="电话")


class Teach(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='extension2')
    name = models.CharField(max_length = 32, verbose_name="姓名")
    age  = models.IntegerField(default=0, verbose_name="年龄")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name="性别")
    id_num = models.CharField(max_length = 18, verbose_name="身份证号")
    field = models.CharField(max_length = 64, verbose_name="教育领域")
    limyear = models.IntegerField(default=0, verbose_name="从教年限")
    fitage = models.IntegerField(verbose_name="教育适合年龄")
    email = models.EmailField(verbose_name="邮箱")
    phone = models.CharField(max_length = 20, verbose_name="电话")
    brief = models.CharField(max_length = 40, verbose_name="简介")


class Inst(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='extension3')
    id_num = models.CharField(max_length = 18, verbose_name="标识码")
    address = models.CharField(max_length = 64, verbose_name="店面地址")
    field = models.CharField(max_length = 64, verbose_name="教育领域")
    fitage = models.IntegerField(verbose_name="教育适合年龄")
    email = models.EmailField(verbose_name="邮箱")
    phone = models.CharField(max_length = 20, verbose_name="电话")
    brief = models.CharField(max_length = 40, verbose_name="简介")


class Admin(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='extension4')

