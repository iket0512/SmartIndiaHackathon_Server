from django.shortcuts import render
from user_datas.models import *
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import requests
import operator
from django.http import JsonResponse

def survey(request):
	response_json={}
	if(request.method=='GET'):
		try:
			user_type=request.GET.get('type')
			# 1-student
			# 2-prof
			access_token=request.GET.get('access_token')
			title=request.GET.get('title')
			description=request.GET.get('description')
			question1=request.GET.get('ques1')
			question2=request.GET.get('ques2')
			question3=request.GET.get('ques3')
			question4=request.GET.get('ques4')
			file=request.FILES.get('file').name
		except Exception,e:
			print e
			response_json['success']=False
			response_json['message']='some error in receiving data'
			return JsonResponse(response_json)
		print file
		try:
			if(str(file)!="None"):
				print "line 19"
				file_name='media/resources/'+str(timezone.now())[:18].replace(" ", "")
				file_name+=file
				fout = open(file_name,'w')
				print "line 21"
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
			set_attr(row,'user_type',user_type)
			set_attr(row,'title',title)
			set_attr(row,'description',description)
			set_attr(row,'question1',question1)
			set_attr(row,'question2',question2)
			set_attr(row,'question3',question3)
			set_attr(row,'question4',question4)
			set_attr(row,'permission',file_name)
			row.save()
			response_json['success']=True
			response_json['message']='survey updated'
			return JsonResponse(response_json)
		except Exception,e:
			row=survey_data.objects.create(access_token=access_token,
				user_type=user_type,title=title,description=description,
				question1=question1,question4=question4,question3=question3,
				question2=question2,permission=file_name)
			response_json['success']=True
			response_json['message']='survey created'
			return JsonResponse(response_json)




				






# Create your views here.
