from __future__ import unicode_literals

from django.db import models

# Create your models here.
class survey_data(models.Model):
	survey_id=models.AutoField(primary_key=True)
	access_token=models.CharField(max_length=250,blank=True,null=True)
	user_type=models.IntegerField(default=1)
	title=models.CharField(max_length=80,blank=True,null=True)
	description=models.CharField(max_length=500,blank=True,null=True)
	question1=models.CharField(max_length=120,blank=True,null=True)
	question2=models.CharField(max_length=120,blank=True,null=True)
	question3=models.CharField(max_length=120,blank=True,null=True)
	question4=models.CharField(max_length=120,blank=True,null=True)
	permission=models.FileField(upload_to='resources',null=True,blank=True)
	modified= models.DateField(auto_now=True,auto_now_add=False,null=True)
	created= models.DateField(auto_now=False,auto_now_add=True,null=True)



