# Generated by Django 2.2.2 on 2019-06-27 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20190627_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_comment',
            name='comment_parent',
            field=models.ForeignKey(db_column='parent_id', on_delete=django.db.models.deletion.CASCADE, to='User.Parent', verbose_name='评价者'),
        ),
    ]