# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-27 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_datas', '0002_auto_20170326_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=800, null=True)),
                ('date', models.DateField()),
                ('field', models.CharField(max_length=400)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='student_data',
            fields=[
                ('student_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('emailid', models.CharField(max_length=30, null=True)),
                ('institution', models.CharField(max_length=50, null=True)),
                ('skills', models.CharField(max_length=400, null=True)),
                ('place', models.CharField(max_length=30, null=True)),
                ('current_year', models.CharField(max_length=20, null=True)),
                ('degree', models.CharField(max_length=50, null=True)),
                ('experience', models.CharField(max_length=1000, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resources/')),
                ('image', models.FileField(blank=True, null=True, upload_to='resources/')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='prof_data',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='prof_data',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
