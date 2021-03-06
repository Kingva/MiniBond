# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-28 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniBond', '0007_auto_20170924_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickTrace',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cookieId', models.UUIDField()),
                ('areaType', models.CharField(max_length=30)),
                ('target', models.CharField(max_length=30)),
                ('propertyData', models.CharField(max_length=30)),
                ('clickTime', models.DateTimeField()),
            ],
        ),
    ]
