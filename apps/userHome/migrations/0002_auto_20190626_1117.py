# Generated by Django 2.2.2 on 2019-06-26 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userHome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tlesson',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course_Base', verbose_name='视听课程'),
        ),
    ]
