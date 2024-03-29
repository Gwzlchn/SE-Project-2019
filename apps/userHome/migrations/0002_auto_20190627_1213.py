# Generated by Django 2.2.2 on 2019-06-27 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userHome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp_lesson',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tll', to='course.Course_Base', verbose_name='视听课程'),
        ),
        migrations.AlterField(
            model_name='temp_lesson',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tlp', to='User.Parent', verbose_name='试听用户'),
        ),
        migrations.AlterField(
            model_name='temp_lesson',
            name='state',
            field=models.CharField(default='待审核', max_length=8),
        ),
    ]
