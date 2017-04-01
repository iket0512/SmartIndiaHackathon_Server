from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import requests
import operator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_datas.models import prof_data
from incubators.models import *
import fuzzywuzzy.fuzz as fuzz
from unidecode import unidecode
from incubators.models import incubators_data
from equipment.models import equipment_data
# Create your views here.

def list1(request):
	fuzz.partial_token_sort_ratio
	try:
		# type1=1
		# city='zz'
		# topic='zz'
		type1=request.GET.get('type')
		city=request.GET.get('city')
		topic=request.GET.get('topic')
		print type1
		print city
		print topic
	except	Exception,e:
		print e
		response_json['success']=False
		response_json['message']='Data not received properly'
		return response_json
	flag=0
	if(city!='zz' and topic=='zz'):
		flag=1
	elif(city=='zz' and topic!='zz'):
		flag=2
	elif(city!='zz' and topic!='zz'):
		flag=3
	response_json={}
	response_json['city_list']=[]
	response_json['topic_list']=[]
	print '43'
	try:
		print 'here after try'
		if(type1=='1'):
			response_json['type']='1'
			city_list=equipment_data.objects.values('city').distinct()
			topic_list=equipment_data.objects.values('institute').distinct()
		elif(type1=='2'):
			response_json['type']='2'
			city_list=incubators_data.objects.values('city').distinct()
			topic_list=equipment_data.objects.filter(institute='Incubator')
		elif(type1=='3'):
			response_json['type']='3'
			city_list=biotech_data.objects.values('city').distinct()
			topic_list=equipment_data.objects.filter(institute='Biotech Park')
		elif(type1=='4'):
			response_json['type']='4'
			city_list=institute_data.objects.values('city').distinct()
			topic_list=equipment_data.objects.filter(institute='Other Institutes')
		elif(type1=='5'):
			response_json['type']='5'
			city_list=incubators_data.objects.values('city').distinct()
			topic_list=survey_data.objects.values('field').distinct()
		elif(type1=='6'):
			response_json['type']='6'
			city_list=student_data.objects.values('city').distinct()
			topic_list=student_data.objects.values('specialization').distinct()
		elif(type1=='7'):
			response_json['type']='7'
			city_list=research_data.objects.values('city').distinct()
			topic_list=research_data.objects.values('field').distinct()
		try:
			for o in city_list:
				temp={}
				print 'adding city'
				temp['city']=str(o['city'])
				response_json['city_list'].append(temp)
		except Exception,e:
			print e
			print 'error in city'
			temp={}
			temp['city']="unavailable"
			response_json['city_list'].append(temp)

		try: 
			for o in topic_list:
				if(type1=='1'):
					temp={}
					print 'adding topic in 1'
					temp['topic']=str(o['institute'])
					response_json['topic_list'].append(temp)
				elif(type1=='2' or type1=='3' or type1=='4'):
					temp={}
					print 'adding topic in 2,3,4'
					temp['topic']=str(o.name)
					response_json['topic_list'].append(temp)
				elif(type1=='5' or type1=='7'):
					temp={}
					print 'adding topic in 5,7'
					temp['topic']=str(o['field'])
					response_json['topic_list'].append(temp)
				elif(type1=='6'):
					temp={}
					print 'adding topic in 6'
					temp['topic']=str(o['specialization'])
					response_json['topic_list'].append(temp)
		except Exception,e:
			print e
			print 'error in topic'
			temp={}
			temp['topic']='unavailable'
			response_json['topic_list'].append(temp)

	except Exception,e:
		print e
		print 'error somewhere in city and topic'
		temp={}
		temp['city']="unavailable"
		response_json['city_list'].append(temp)
		temp['city']='unavailable'
		response_json['city_list'].append(temp)

	if(request.method=='GET'):
		response_json['success']=True
###############################################################################3		
		if(type1=='1'):
			try:
				response_json['institutionItemDataList']=[]
				if (flag==0 or flag==2):
					filtered_list= equipment_data.objects.all()
				elif (flag==1 or flag==3):
					filtered_list= equipment_data.objects.filter(city=city)
				for item in filtered_list:
					allowed=True
					if(flag==2 or flag==3):
						ratio=fuzz.partial_token_sort_ratio(unidecode(topic),unidecode(o.institute))*7.5/10+fuzz.token_sort_ratio(unidecode(topic),unidecode(o.institute))*2.5/10
						if(ratio<75):
							allowed=False
					if(allowed):
						details={}
						details['id']=str(o.equipment_id)
						details['name']=str(o.name)
						details['specialization']=str(o.features)
						details['image']=str(o.photo)
						response_json['institutionItemDataList'].append(details)
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']="Error in facilities list"
				return JsonResponse(response_json)
				######################################			
# incubators  ####
		elif(type1=='2'):
			try:
				response_json['institutionItemDataList']=[]
				if (flag==0 or flag==2):
					filtered_list= incubators_data.objects.all()
				elif (flag==1 or flag==3):
					filtered_list= incubators_data.objects.filter(city=city)
				for o in filtered_list:
					allowed=True
					if(flag==2 or flag==3):
						ratio1=fuzz.partial_token_sort_ratio(unidecode(topic),unidecode(o.facilities))*7.5/10+fuzz.token_sort_ratio(unidecode(topic),unidecode(o.facilities))*2.5/10
						if(ratio1<75):
							allowed=False
					if(allowed):
						details={}
						details['id']=str(o.incubator_id)
						details['name']=str(o.name)
						details['place']=str(o.city)
						details['image']=str(o.image)
						details['email']=str(o.website)
						response_json['institutionItemDataList'].append(details)
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']="Error in incubators list"
				return JsonResponse(response_json)
				###########################################
# biotech parks#####
		elif(type1=='3'):
			try:
				response_json['institutionItemDataList']=[]
				if (flag==0 or flag==2):
					filtered_list= biotech_data.objects.all()
				elif (flag==1 or flag==3):
					filtered_list= biotech_data.objects.filter(city=city)
				for o in filtered_list:
					allowed=True
					if(flag==2 or flag==3):
						ratio1=fuzz.partial_token_sort_ratio(unidecode(topic),unidecode(o.facilities))*7.5/10+fuzz.token_sort_ratio(unidecode(topic),unidecode(o.facilities))*2.5/10
						if(ratio1<75):
							allowed=False
					if(allowed):
						details={}
						details['id']=str(o.biotech_id)
						details['name']=str(o.name)
						details['place']=str(o.city)
						details['email']=str(o.website)
						response_json['institutionItemDataList'].append(details)
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']="Error in incubators list"
				return JsonResponse(response_json)
	#########################################################
#institution####				
		elif(type1=='4'):
			try:
				response_json['institutionItemDataList']=[]
				if (flag==0 or flag==2):
					filtered_list= institute_data.objects.all()
				elif (flag==1 or flag==3):
					filtered_list= institute_data.objects.filter(city=city)
				for o in filtered_list:
					allowed=True
					if(flag==2 or flag==3):
						ratio1=fuzz.partial_token_sort_ratio(unidecode(topic),unidecode(o.facilities))*7.5/10+fuzz.token_sort_ratio(unidecode(topic),unidecode(o.facilities))*2.5/10
						if(ratio1<75):
							allowed=False
					if(allowed):
						details={}
						details['id']=str(o.institute_id)
						details['name']=str(o.name)
						details['city']=str(o.city)
						details['website']=str(o.website)
						response_json['institutionItemDataList'].append(details)
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']="Error in incubators list"
				return JsonResponse(response_json)

		##########################################################
	#survey			
		elif(type1=='5'):
			try:
				response_json['surveyItemDataList']=[]
				if (flag==0 or flag==2):
					filtered_list=survey_data.objects.all()
				elif (flag==1 or flag==3):
					filtered_list=survey_data.objects.filter(city=city)
				for o in filtered_list:
					allowed=True
					if(flag==2 or flag==3):
						ratio1=fuzz.partial_token_sort_ratio(unidecode(topic),unidecode(o.field))*7.5/10+fuzz.token_sort_ratio(unidecode(topic),unidecode(o.field))*2.5/10
						if(ratio1<75):
							allowed=False
					if(allowed):
						details={}
						details['id']=str(o.survey_id)
						details['title']=str(o.title)
						details['city']=str(o.city)
						details['filled']=str(o.filled)
						response_json['surveyItemDataList'].append(details)
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']="Error in incubators list"
				return JsonResponse(response_json)

	########################################################################
	#			

	print str(response_json)

	return JsonResponse(response_json)


		
				





	







