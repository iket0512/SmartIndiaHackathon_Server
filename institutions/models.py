from __future__ import unicode_literals

from django.db import models

# Create your models here.
class institute_data(models.Model):
	institute_id= models.AutoField(primary_key=True)
	image=models.CharField(max_length=5000,null=True)
	name=models.CharField(max_length=100,null=False)
	city=models.CharField(max_length=100,null=True,blank=True)
	address=models.CharField(max_length=100,null=True,blank=True)
	phone=models.CharField(max_length=13,null=True)
	website=models.CharField(max_length=100,null=True)
	latitude=models.CharField(max_length=25,blank=True,null=True)
	longitude=models.CharField(max_length=25,blank=True,null=True)
