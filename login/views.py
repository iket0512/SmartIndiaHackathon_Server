from django.shortcuts import render
from user_datas.models import *
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import requests
import operator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage,get_connection
from django.contrib.auth.models import User
from django.contrib.auth.views import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django import forms
import random
# try:
#     from cStringIO import StringIO
# except ImportError:
#     from StringIO import StringIO
from django.core.mail.backends.smtp import EmailBackend

@csrf_exempt
def prof_login(request):
	if(request.method=='GET'):
		response_json={}
		try:
			email=str('ikykota@gmail.com')
			name=str('iket')
			# name=request.POST.get('name')
			# email=request.POST.get('email')
		except Exception,e:
			print e
			response_json['success']=False
			response_json['message']='Error in accepting email'
			return JsonResponse(response_json)
		backend = EmailBackend(host='smtp.gmail.com', port=587, username='iket.ag24@gmail.com', 
                       password='uzugbuhubijhfnuv', use_tls=True, fail_silently=True)
		otp=random.randint(100000,999999)
		body="""Hello sir,
Your password for login in biotechnology professors data is %s
Thanks & Regards.
Iket Agrawal
Team invincibles."""				
		EmailMsg=EmailMessage("SmartIndia Hackathon",body %(str(otp)),'no-reply@gmail.com',[email],connection=backend)
		# pdf = pdfkit.from_url('http://127.0.0.1:8000/test1/',False)
		# value= str(request.POST.get('yesno'))
		# if value=="yes":
		# 	file=request.FILES['file']
		# 	EmailMsg.attach(file.name,file.read() ,file.content_type)
		EmailMsg.send()
		try:
			otp_row=prof_data.objects.get(emailid=email)
			set_attr(otp_row,'name',name)
			set_attr(otp_row,'flag',False)
			otp_row.save()
			response_json['success']=True
			response_json['message']='Email sent again for verification'
		except Exception,e:
			print e
			otp_row=prof_data.objects.create(emailid=email,name=name,flag=False)
			response_json['success']=True
			response_json['message']='Email sent for verification'
		return JsonResponse(response_json)

@csrf_exempt
def student_login(request):
	if(request.method=='POST'):
		response_json={}
		try:
			stu_id=request.POST.get('id')
			name=request.POST.get('name')
			email=request.POST.get('email')
		except Exception,e:
			print e
			print 'unable to get info'
			response_json['success']=False
			response_json['message']='unable to get info'
			return JsonResponse(response_json)

		try:
			student_row=student_data.objects.get(student_id=stu_id)
			set_attr(student_row,'name',name)
			set_attr(student_row,'email',emailid)
			student_row.save()
			response_json['success']=True
			return JsonResponse(response_json)
		except Exception,e:
			student_row=student.objects.create(student_id=stu_id,name=name,emailid=email)
			response_json['success']=True
			return JsonResponse(response_json)


# Create your views here.
