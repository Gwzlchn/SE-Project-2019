from django.db import models

# Create your models here.
from apps.User.models import POS

class tlesson(models.Model):
    person = models.ForeignKey(POS,on_delete=models.CASCADE,verbose_name='视听用户')