# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2020-03-15 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0003_auto_20200315_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='housecollection',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='housecollection',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='收藏/取消时间'),
        ),
    ]
