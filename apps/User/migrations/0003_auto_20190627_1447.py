# Generated by Django 2.2.2 on 2019-06-27 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CHINA_LOCATION', '0001_initial'),
        ('User', '0002_auto_20190627_0226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='Address',
        ),
        migrations.AddField(
            model_name='branch',
            name='branch_city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='branch_city', to='CHINA_LOCATION.ChinaLocation', verbose_name='所在城市'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='branch_distinct',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='branch_distinct', to='CHINA_LOCATION.ChinaLocation', verbose_name='所在区'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='branch_province',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='branch_province', to='CHINA_LOCATION.ChinaLocation', verbose_name='所在省份'),
            preserve_default=False,
        ),
    ]
