# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-01 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_datas', '0011_student_data_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
