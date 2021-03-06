# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fei', '0005_auto_20160520_0716'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChiFan_Sep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='chifan',
            name='total',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chifan_sep',
            name='chifan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fei.ChiFan'),
        ),
        migrations.AddField(
            model_name='chifan_sep',
            name='ren',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fei.Ren'),
        ),
    ]
