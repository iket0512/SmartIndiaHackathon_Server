# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-01 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biotechpark', '0002_biotech_data_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biotech_data',
            name='image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='biotech_data',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]