# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fei', '0002_auto_20160520_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='charge',
            name='money',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
