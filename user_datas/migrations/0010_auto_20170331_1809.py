# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-31 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_datas', '0009_auto_20170331_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof_data',
            name='facilities',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prof_data',
            name='latitude',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='prof_data',
            name='longitude',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='student_data',
            name='year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
