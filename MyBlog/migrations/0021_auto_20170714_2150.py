# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0020_auto_20170714_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='static/img/no-img.jpg', upload_to='MyBlog/static/img/Blog/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='MyBlog/static/img/no-img.jpg', upload_to='MyBlog/static/img/post/'),
        ),
    ]
