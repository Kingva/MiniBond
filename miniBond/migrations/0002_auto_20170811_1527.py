# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-11 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniBond', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='website',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='platformrating',
            name='url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='promotioninfo',
            name='url',
            field=models.URLField(default=''),
        ),
    ]