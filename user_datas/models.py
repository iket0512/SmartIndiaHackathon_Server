from __future__ import unicode_literals

from django.db import models

# Create your models here.
class prof_data(models.Model):
	p_id= models.AutoField(primary_key=True)
	otp=models.IntegerField(default=0)
	flag=models.BooleanField(default=False)
	image=models.CharField(max_length=100,null=True)
	name=models.CharField(max_length=100,null=False)
	designation=models.CharField(max_length=100,null=True)
	phone=models.CharField(max_length=13,null=True)
	emailid=models.CharField(max_length=30,null=True)
	specialization=models.CharField(max_length=100,null=True)
	affliation=models.CharField(max_length=100,null=True)
	affliation_type=models.IntegerField(null=True)
	city=models.CharField(max_length=50,null=True,blank=True)
	edu_degree=models.CharField(max_length=100,null=True)
	edu_institute=models.CharField(max_length=100,null=True)
	papers=models.CharField(max_length=100,null=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False,null=True)
	created= models.DateTimeField(auto_now=False,auto_now_add=True,null=True)

class student_data(models.Model):
	student_id=models.CharField(max_length=200,primary_key=True)
	name=models.CharField(max_length=50,null=False)
	emailid=models.CharField(max_length=30,null=True)
	institution=models.CharField(max_length=50,null=True,blank=True)
	skills=models.CharField(max_length=400,null=True,blank=True)
	place=models.CharField(max_length=30,null=True,blank=True)
	current_year=models.CharField(max_length=20,null=True,blank=True)
	degree=models.CharField(max_length=50,null=True,blank=True)
	experience=models.CharField(max_length=1000,null=True,blank=True)
	resume=models.FileField(upload_to='resources/',null=True,blank=True)
	image=models.FileField(upload_to='resources/',null=True,blank=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

class projects(models.Model):
	project_id=models.AutoField(primary_key=True)
	student_id=models.ForeignKey(student_data,to_field='student_id',default='1')
	title=models.CharField(max_length=100,null=False)
	description=models.CharField(max_length=800,null=True)
	date=models.DateField()
	field=models.CharField(max_length=400)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

