from __future__ import unicode_literals

from django.db import models


class research_data(models.Model):
	survey_id=models.AutoField(primary_key=True)
	access_token=models.CharField(max_length=250,blank=True,null=True)
	title=models.CharField(max_length=80,blank=True,null=True)
	description=models.CharField(max_length=500,blank=True,null=True)
	city=models.CharField(max_length=500,blank=True,null=True)
	field=models.CharField(max_length=100,blank=True,null=True)
	modified= models.DateField(auto_now=True,auto_now_add=False,null=True)
	created= models.DateField(auto_now=False,auto_now_add=True,null=True)

# Create your models here.
