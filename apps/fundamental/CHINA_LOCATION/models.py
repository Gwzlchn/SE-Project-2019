from django.db import models


# Create your models here.
class ChinaLocation(models.Model):
    id = models.SmallIntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=15,verbose_name="区域名称")
    parent_id = models.SmallIntegerField(default=0, db_column='parent_id')
    level = models.SmallIntegerField(null=False,choices=[(1,'省/直辖市'),(2,'市'),(3,'辖区')])
    class Meta:
        db_table = 'CHINA_LOCATION'



