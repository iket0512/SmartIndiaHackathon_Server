# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-01 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute_data',
            name='latitude',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='institute_data',
            name='longitude',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]