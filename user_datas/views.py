from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import requests
import operator
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
from .models import *
# Create your views here.

@csrf_exempt
def add_details(request):
	if(request.method=='POST'):
		response_json={}
		try:
			user_id=request.POST.get('access_token')
			user_type=request.POST.get('key_type')
			institution=request.POST.get('user_institution')
			skills=request.POST.get('user_skills')
			place=request.POST.get('user_place')
			year=request.POST.get('year')
			specialization=request.POST.get('specialization')
			degree=request.POST.get('qualification')
			experience=request.POST.get('user_experience')
			print 'line 26'
			file=request.FILES.get('file').name
			print user_id
			print str(file)
		except Exception,e:
			print e
			print 'exception 1st'
			response_json['success']=False
			response_json['message']='Error in receiving data'
			return JsonResponse(response_json)

		if(str(file)!="None"):
			print "line 37"
			file_name='media/profile/'+str(timezone.now())[:18].replace(" ", "")
			file_name+=file
			fout = open(file_name,'w')
			print "line 41"
			file_content = request.FILES.get('file').read()
			fout.write(file_content)
			fout.close()
			print"file created"	
			response_json['success']=True
			response_json['message']="file uploaded"
		try:
			student_row=student_data.objects.get(student_id=user_id)
			setattr(student_row,'institution',institution)
			setattr(student_row,'type1',user_type)
			setattr(student_row,'specialization',specialization)
			setattr(student_row,'skills',skills)
			setattr(student_row,'place',place)
			setattr(student_row,'year',year)
			setattr(student_row,'degree',degree)
			setattr(student_row,'experience',experience)
			setattr(student_row,'image',file)
			student_row.save()
			response_json['success']=True
		except Exception,e:
			print e
			print 'exception 2nd'
			response_json['success']=False
			response_json['message']='No such student id exists..login again'
	return JsonResponse(response_json)

@csrf_exempt
def upload_to_student(request):
	response_json={}
	if(request.method=='GET'):
		try:
			file_upload_type=int(request.GET.get('type'))
			student_id=request.GET.get('access_token')
			file=request.FILES.get('file').name
			print file
			

			try:
				student_row=student_data.objects.get(student_id=student_id)
				if(file_upload_type==1):
					set_attr(student_row,'resume',file_name)
				elif(file_upload_type==2):
					set_attr(student_row,'image',file_name)
				student_row.save()
			except Exception,e:
				response_json['success']=False
				response_json['message']="error finding student"	
		except Exception,e:
			response_json['success']=False
			response_json['message']="Some error in uploading"	

			# url='sdvsfv'
			# json={}
			# header={}
			# response=requests.post(url,json,header)	

'''
>>> term="tuberclosis"
>>> response=requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term="+term+"&retmode=json")
[u'19008416', u'18927361', u'18787170', u'18487186', u'18239126', u'18239125']
>>> json=response.json()
>>> json['esearchresult']['idlist']
'''







