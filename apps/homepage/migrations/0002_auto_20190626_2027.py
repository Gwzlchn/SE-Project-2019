# Generated by Django 2.2.1 on 2019-06-26 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_order',
            old_name='CO_id',
            new_name='CO',
        ),
        migrations.RenameField(
            model_name='insti_order',
            old_name='IO_id',
            new_name='IO',
        ),
        migrations.RenameField(
            model_name='news_order',
            old_name='NO_id',
            new_name='NO',
        ),
        migrations.RenameField(
            model_name='teacher_order',
            old_name='TO_id',
            new_name='TO',
        ),
        migrations.RenameField(
            model_name='video_order',
            old_name='VO_id',
            new_name='VO',
        ),
    ]
