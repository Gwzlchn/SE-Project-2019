# Generated by Django 2.2.2 on 2019-06-26 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0005_auto_20190626_1447'),
        ('storage', '0003_auto_20190617_1555'),
        ('course', '0001_initial'),
        ('User', '0002_auto_20190627_0226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order', models.IntegerField()),
                ('VO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Video')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order', models.IntegerField()),
                ('TO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='News_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order', models.IntegerField()),
                ('NO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.News')),
            ],
        ),
        migrations.CreateModel(
            name='Insti_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order', models.IntegerField()),
                ('IO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Institution')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order', models.IntegerField()),
                ('CO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course_Base')),
            ],
        ),
    ]
