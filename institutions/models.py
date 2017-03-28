from __future__ import unicode_literals

from django.db import models

# Create your models here.
class institute_data(models.Model):
	institute_id= models.AutoField(primary_key=True)
	image=models.CharField(max_length=100,null=True)
	name=models.CharField(max_length=100,null=False)
	designation=models.CharField(max_length=100,null=True)
	phone=models.CharField(max_length=13,null=True)
	emailid=models.CharField(max_length=30,null=True)
	specialization=models.CharField(max_length=100,null=True)
	affliation=models.CharField(max_length=100,null=True)
	edu_degree=models.CharField(max_length=100,null=True)
	edu_institute=models.CharField(max_length=100,null=True)
	papers=models.CharField(max_length=100,null=True)