# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-29 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_survey_data_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey_data',
            name='field',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]