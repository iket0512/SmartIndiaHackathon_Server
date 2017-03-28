from __future__ import unicode_literals

from django.db import models

# Create your models here.
class incubators_data(models.Model):
	incubator_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=30,blank=False,null=False)
	state=models.CharField(max_length=60,blank=True,null=True)
	city=models.CharField(max_length=60,blank=True,null=True)
	thrust_area=models.CharField(max_length=300,blank=True,null=True)
	address=models.CharField(max_length=300,blank=True,null=True)
	website=models.CharField(max_length=300,blank=True,null=True)
	contact_name=models.CharField(max_length=50,blank=True,null=True)
	contact_designation=models.CharField(max_length=300,blank=True,null=True)
	contact_email=models.CharField(max_length=300,blank=True,null=True)
	contact_phone=models.CharField(max_length=13,blank=True,null=True)