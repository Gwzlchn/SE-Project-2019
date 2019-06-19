# Generated by Django 2.2.2 on 2019-06-18 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tlesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='视听课程')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Parent', verbose_name='试听用户')),
            ],
        ),
    ]