# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 08:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fei', '0007_chifan_const_share'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chifan',
            old_name='const_share',
            new_name='cost_sharing',
        ),
    ]
