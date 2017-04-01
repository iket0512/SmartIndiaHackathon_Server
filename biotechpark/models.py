from __future__ import unicode_literals

from django.db import models

class biotech_data(models.Model):
	biotech_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=100,blank=False,null=False)
	city=models.CharField(max_length=60,blank=True,null=True)
	facilities=models.CharField(max_length=100,blank=True,null=True)
	address=models.CharField(max_length=300,blank=True,null=True)
	website=models.CharField(max_length=300,blank=True,null=True)
	contact_name=models.CharField(max_length=50,blank=True,null=True)
	contact_designation=models.CharField(max_length=300,blank=True,null=True)
	contact_email=models.CharField(max_length=300,blank=True,null=True)
	contact_phone=models.CharField(max_length=13,blank=True,null=True)
	latitude=models.CharField(max_length=25,blank=True,null=True)
	image=models.CharField(max_length=1000,blank=True,null=True)
	longitude=models.CharField(max_length=25,blank=True,null=True)

# Create your models here.
