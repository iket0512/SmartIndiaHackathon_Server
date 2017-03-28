# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-28 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_datas', '0005_auto_20170327_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof_data',
            name='flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='prof_data',
            name='otp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='current_year',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='degree',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='experience',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='institution',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='place',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='skills',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
