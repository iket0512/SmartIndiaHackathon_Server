from __future__ import unicode_literals

from django.db import models

class equipment_data(models.Model):
	equipment_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=150,blank=False,null=False)
	photo=models.CharField(max_length=1250,blank=True,null=True)
	description=models.CharField(max_length=550,blank=True,null=True)
	use=models.CharField(max_length=500,blank=True,null=True)
	features=models.CharField(max_length=250,blank=True,null=True)
	city=models.CharField(max_length=100,blank=True,null=True)
	institute=models.CharField(max_length=100,blank=True,null=True)
	institute_id=models.CharField(max_length=100,blank=True,null=True)
# Create your models here.
