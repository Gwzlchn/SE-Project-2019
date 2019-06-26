# Generated by Django 2.2.1 on 2019-06-26 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
        ('course', '0003_course_base_course_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_institution',
            name='course_ins',
        ),
        migrations.AddField(
            model_name='course_institution',
            name='course_ins',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Ins_for_Course', to='User.Institution', verbose_name='机构名称'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='course_teacher',
            name='course_teacher',
        ),
        migrations.AddField(
            model_name='course_teacher',
            name='course_teacher',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Teacher_for_course', to='User.Teacher', verbose_name='教师名称'),
            preserve_default=False,
        ),
    ]
