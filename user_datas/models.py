from __future__ import unicode_literals

from django.db import models

# Create your models here.
class prof_data(models.Model):
	p_id= models.AutoField(primary_key=True)
	otp=models.IntegerField(default=0)
	flag=models.BooleanField(default=False)
	image=models.CharField(max_length=100,null=True,blank=True)
	name=models.CharField(max_length=100,null=False,blank=True)
	phone=models.CharField(max_length=13,null=True,blank=True)
	website=models.CharField(max_length=60,null=True,blank=True)
	emailid=models.CharField(max_length=30,null=True,blank=True)
	city=models.CharField(max_length=50,null=True,blank=True)
	facilities=models.CharField(max_length=100,null=True,blank=True)
	latitude=models.CharField(max_length=25,blank=True,null=True)
	longitude=models.CharField(max_length=25,blank=True,null=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False,null=True)
	created= models.DateTimeField(auto_now=False,auto_now_add=True,null=True)

class student_data(models.Model):
	student_id=models.CharField(max_length=200,primary_key=True)
	name=models.CharField(max_length=50,null=False)
	emailid=models.CharField(max_length=90,null=True)
	type1=models.IntegerField(default=0,blank=True,null=False)
	institution=models.CharField(max_length=50,null=True,blank=True)
	skills=models.CharField(max_length=400,null=True,blank=True)
	year=models.CharField(max_length=100,null=True,blank=True)
	specialization=models.CharField(max_length=200,blank=True,null=True)
	city=models.CharField(max_length=30,null=True,blank=True)
	degree=models.CharField(max_length=50,null=True,blank=True)
	experience=models.CharField(max_length=1000,null=True,blank=True)
	resume=models.FileField(upload_to='resources/',null=True,blank=True)
	image=models.ImageField(upload_to="profile",null=True,blank=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

