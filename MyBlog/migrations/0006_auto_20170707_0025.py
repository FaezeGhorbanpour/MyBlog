# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0005_auto_20170706_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyBlog.User'),
        ),
    ]