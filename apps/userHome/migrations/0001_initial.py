# Generated by Django 2.2.2 on 2019-06-26 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('User', '0002_auto_20190627_0226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp_Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(default='未通过', max_length=8)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course_Base', verbose_name='视听课程')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Parent', verbose_name='试听用户')),
            ],
        ),
    ]
