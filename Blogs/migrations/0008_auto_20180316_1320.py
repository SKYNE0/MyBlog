# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0007_auto_20180316_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateTimeField(verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150, unique=True, verbose_name='标题'),
        ),
    ]