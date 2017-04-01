from django.shortcuts import render
from user_datas.models import *
from django.utils import timezone
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import operator
from django.http import JsonResponse

@csrf_exempt
def survey_upload(request):
	response_json={}
	if(request.method=='POST'):
		try:
			user_type=request.POST.get('type')
			# 1-student/prof
			# 2-institute
			access_token=request.POST.get('access_token')
			title=request.POST.get('title')
			description=request.POST.get('description')
			question1=request.POST.get('ques1')
			question2=request.POST.get('ques2')
			question3=request.POST.get('ques3')
			question4=request.POST.get('ques4')
			field=request.POST.get('field').name
			print title
			print description
			print question2
			print question4
			print question3
			print question1
			file=request.FILES.get('file').name
			print 2
		except Exception,e:
			print e
			response_json['success']=False
			response_json['message']='some error in receiving data'
			return JsonResponse(response_json)
		print file
		try:
			if(str(file)!="None"):
				file_name='media/resources/'+str(timezone.now())[:18].replace(" ", "")
				# file_name='resources/'
				# print "line 20"+file_name
				file_name+=file
				# print "line 21"+file_name
				fout = open(file_name,'w')
				# print "line 22"
				file_content = request.FILES.get('file').read()
				fout.write(file_content)
				fout.close()
				print"file created"
		except Exception,e:
			response_json['success']=False
			response_json['message']='error in file creation'
			return JsonResponse(response_json)
		try:
			row=survey_data.objects.get(access_token=access_token)
			print 3
			setattr(row,'user_type',user_type)
			setattr(row,'title',title)
			setattr(row,'field',field)
			setattr(row,'description',description)
			setattr(row,'question1',question1)
			setattr(row,'question2',question2)
			setattr(row,'question3',question3)
			setattr(row,'question4',question4)
			setattr(row,'permission',file_name)
			row.save()
			response_json['success']=True
			response_json['message']='survey updated'
			print 33
			return JsonResponse(response_json)
		except Exception,e:
			print 4
			row=survey_data.objects.create(access_token=access_token,
				user_type=user_type,title=title,description=description,
				question1=question1,field=field,question4=question4,question3=question3,
				question2=question2,permission=file_name)
			response_json['success']=True
			response_json['message']='survey created'
			print 44
			return JsonResponse(response_json)

@csrf_exempt
def survey_upload(request):
	response_json={}
	if(request.method=='POST'):
		survey_id=request.POST.get('id')
		answer1=request.POST.get('ans1')
		answer2=request.POST.get('ans2')
		answer3=request.POST.get('ans3')
		answer4=request.POST.get('ans4')
		access_token=request.POST.get('access_token')
	try:	
		row=survey_submitted.objects.get(survey_id=survey_id)
		if(row.access_token==access_token):
			response_json['success']=False
			response_json['message']='Response already submitted before'
			return JsonResponse(response_json)
	except Exception,e:
		row=survey_submitted.objects.create(survey_id=survey_id,access_token=access_token,answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4)
		response_json['success']=True
		response_json['message']='Response added successfully'
		return JsonResponse(response_json)
			









				






# Create your views here.
