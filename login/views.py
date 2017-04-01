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

def prof_signup(request):
	print 'start'
	if(request.method=='GET'):
		print 'get method'
		response_json={}
		try:
			# email=str('ikykota@gmail.com')
			# name=str('iket')
			name=request.GET.get('name')
			email=request.GET.get('email')
			print name
			print email
		except Exception,e:
			print e
			response_json['success']=False
			response_json['message']='Error in accepting email id'
			print str(response_json)
			return JsonResponse(response_json)
		otp=random.randint(100000,999999)	
		try:	
			backend = EmailBackend(host='smtp.gmail.com', port=587, username='iket.ag24@gmail.com', 
	                       password='uzugbuhubijhfnuv', use_tls=True, fail_silently=True)
			body="""Hello sir,
					Your password for login in as an Institution is %s
					Thanks & Regards.
					Iket Agrawal
					Team invincibles."""				
			EmailMsg=EmailMessage("SmartIndia Hackathon",body %(str(otp)),'no-reply@gmail.com',[email],connection=backend)
			# pdf = pdfkit.from_url('http://127.0.0.1:8000/test1/',False)
			# value= str(request.POST.get('yesno'))
			# if value=="yes":
			# 	file=request.FILES['file']
			# 	EmailMsg.attach(file.name,file.read() ,file.content_type)
			print 'sending mail'
			EmailMsg.send()
			print 'email sent'
		except Exception,e:
			print e
			print 'email not sent'
			response_json['success']=False
			response_json['message']='Email not sent'
			print str(response_json)
			return JsonResponse(response_json)
		try:
			otp_row=prof_data.objects.get(emailid=email)
			setattr(otp_row,'name',name)
			setattr(otp_row,'otp',otp)
			setattr(otp_row,'flag',False)
			otp_row.save()
			response_json['success']=True
			response_json['message']='Email sent again for verification'
		except Exception,e:
			print e
			otp_row=prof_data.objects.create(emailid=email,name=name,flag=False,otp=otp)
			response_json['success']=True
			response_json['message']='Email sent for verification'
		return JsonResponse(response_json)

def prof_login(request):
	if(request.method=='GET'):
		response_json={}
		# email='iket@codenicely.in'
		# otp='555'
		email=request.GET.get('email')
		otp=request.GET.get('pass')
		print email
		print otp
		try:
			row=prof_data.objects.get(emailid=email)
			print row.otp
			if(row.otp==int(otp)):
				setattr(row,'flag',True)
				response_json['success']=True
				response_json['access_token']=str(row.p_id)
				response_json['message']='OTP Verified.'
				row.save()
				return JsonResponse(response_json)
			else:
				response_json['success']=False
				response_json['message']='OTP Incorrect.'
				return JsonResponse(response_json)
		except Exception,e:
			print e
			response_json['success']=False
			response_json['message']='Email id does not exist.'
			return JsonResponse(response_json)

def student_login(request):
	if(request.method=='GET'):
		response_json={}
		try:
			stu_id=request.GET.get('id')
			name=request.GET.get('name')
			email=request.GET.get('email')
			print stu_id
			print name
			print email
		except Exception,e:
			print e
			print 'unable to get info'
			response_json['success']=False
			response_json['message']='unable to get info'
			return JsonResponse(response_json)
		try:
			student_row=student_data.objects.get(student_id=stu_id)
			setattr(student_row,'name',name)
			setattr(student_row,'emailid',email)
			student_row.save()
			response_json['success']=True
			response_json['access_token']=str(stu_id)
			return JsonResponse(response_json)
		except Exception,e:
			print e
			student_row=student_data.objects.create(student_id=stu_id,name=name,emailid=email)
			response_json['success']=True
			response_json['access_token']=str(stu_id)
			return JsonResponse(response_json)
# Create your views here.
