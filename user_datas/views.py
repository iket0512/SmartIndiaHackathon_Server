from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import requests
import operator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_datas.models import *
# Create your views here.

@csrf_exempt
def add_student_details(request):
	if(request.method=='GET'):
		response_json={}
		try:
			stu_id=request.GET.get('id')
			institution=request.GET.get('institution')
			skills=request.GET.get('skills')
			place=request.GET.get('place')
			current_year=request.Get.get('current_year')
			degree=request.GET.get('degree')
			experience=request.GET.get('experience')
		except Exception.e:
			print e
			response_json['success']=False
			response_json['message']='Error in receiving data'
			return
		try:	
			student_row=student_data.objects.get(student_id=stu_id)
			set_attr(student_row,'institution',institution)
			set_attr(student_row,'skills',skills)
			set_attr(student_row,'place',place)
			set_attr(student_row,'current_year',current_year)
			set_attr(student_row,'degree',degree)
			set_attr(student_row,'experience',experience)
			student_row.save()
			response_json['success']=True
		except Exception,e:
			print e
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

			response_json['success']=True
			response_json['message']="file uploaded"
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







