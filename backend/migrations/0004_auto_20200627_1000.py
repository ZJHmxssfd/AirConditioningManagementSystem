# Generated by Django 3.0.6 on 2020-06-27 02:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200627_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturesensor',
            name='last_update',
            field=models.TimeField(default=datetime.datetime(2020, 6, 27, 2, 0, 50, 616305, tzinfo=utc), verbose_name='上次更新时间'),
        ),
    ]
