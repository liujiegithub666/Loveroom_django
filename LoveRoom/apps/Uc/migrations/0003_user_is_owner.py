# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-14 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uc', '0002_auto_20190806_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_owner',
            field=models.BooleanField(default=False, verbose_name='是否是房东'),
        ),
    ]
