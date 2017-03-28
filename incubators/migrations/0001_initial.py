# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-27 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='incubators_data',
            fields=[
                ('incubator_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('thrust_area', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('website', models.CharField(max_length=300)),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_designation', models.CharField(max_length=300)),
                ('contact_email', models.CharField(max_length=300)),
                ('contact_phone', models.CharField(max_length=13)),
            ],
        ),
    ]