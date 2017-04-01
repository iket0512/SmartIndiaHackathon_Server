# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-31 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='biotech_data',
            fields=[
                ('biotech_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(blank=True, max_length=60, null=True)),
                ('facilities', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('website', models.CharField(blank=True, max_length=300, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_designation', models.CharField(blank=True, max_length=300, null=True)),
                ('contact_email', models.CharField(blank=True, max_length=300, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=13, null=True)),
                ('latitude', models.CharField(blank=True, max_length=25, null=True)),
                ('longitude', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
    ]