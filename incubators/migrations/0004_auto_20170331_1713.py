# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-31 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incubators', '0003_incubators_data_facilities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incubators_data',
            name='facilities',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='incubators_data',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
