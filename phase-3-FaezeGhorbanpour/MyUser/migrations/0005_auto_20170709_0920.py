# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 04:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyUser', '0004_auto_20170709_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
