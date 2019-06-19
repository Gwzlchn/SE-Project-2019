# Generated by Django 2.2.2 on 2019-06-19 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChinaLocation',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=15, verbose_name='区域名称')),
                ('parent_id', models.SmallIntegerField(db_column='parent_id', default=0)),
                ('level', models.SmallIntegerField(choices=[(1, '省/直辖市'), (2, '市'), (3, '辖区')])),
            ],
            options={
                'db_table': 'CHINA_LOCATION',
            },
        ),
    ]