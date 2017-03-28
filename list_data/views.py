from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import requests
import operator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_datas.models import prof_data
import fuzzywuzzy.fuzz as fuzz
from unidecode import unidecode
from incubators.models import incubators_data
# Create your views here.

def list1(request):
	fuzz.partial_token_sort_ratio
	try:
		type1=0
		city='zz'
		topic='zz'
		# type1=request.GET.get('type')
		# city=request.GET.get('city')
		# topic=request.GET.get('topic')
	except	Exception,e:
		print e
		response_json['success']=False
		response_json['message']='Data not received properly'
		return response_json
	# college=request.GET.get('college')
	flag=0
	if(city!='zz' and topic=='zz'):
		flag=1
	elif(city=='zz' and topic!='zz'):
		flag=2
	elif(city!='zz' and topic!='zz'):
		flag=3
	response_json={}
	if(request.method=='GET'):
		response_json['success']=True
###############################################################################3		
		if(type1==0):
			try:
				response_json['city_list']=[]
				city_list=prof_data.objects.values('city').distinct()
				for o in city_list:
					temp={}
					print 1
					print str(o['city'])
					temp['city']=str(o['city'])
					response_json['city_list'].append(temp)
			except Exception,e:
				print e
				response_json['city_list']=[]
				temp={}
				temp['city']="unavailable"
				response_json['city_list'].append(temp)

			try:
				response_json['prof_details']=[]
				# prof_list=prof_data.objects.order_by('name')[:1000]
				if(flag==1):
					if(city=='Centrally Funded'):
						for o in prof_data.objects.filter(affliation_type=1):
							details={}
							details['id']=str(o.p_id)
							details['name']=str(o.name)
							details['emailid']=str(o.emailid)
							details['specialization']=str(o.specialization)
							details['image']=str(o.image)
							response_json['prof_details'].append(details)
					else:
						for o in prof_data.objects.filter(city=city):
							details={}
							details['id']=str(o.p_id)
							details['name']=str(o.name)
							details['emailid']=str(o.emailid)
							details['specialization']=str(o.specialization)
							details['image']=str(o.image)
							response_json['prof_details'].append(details)
				elif(flag==2):
					for o in prof_data.objects.all():
						ratio=fuzz.partial_token_sort_ratio(unidecode(topic),unidecode(o.specialization))*7.5/10+fuzz.token_sort_ratio(unidecode(topic),unidecode(o.specialization))*2.5/10
						if(ratio>=75):
							details={}
							details['id']=str(o.p_id)
							details['name']=str(o.name)
							details['emailid']=str(o.emailid)
							details['specialization']=str(o.specialization)
							details['image']=str(o.image)
							response_json['prof_details'].append(details)
				elif(flag>2):
					if(city=='Centrally Funded'):
						for o in prof_data.objects.filter(affliation_type='1'):
							ratio=fuzz.partial_token_sort_ratio(unidecode(topic),unidecode(o.specialization))*7.5/10+fuzz.token_sort_ratio(unidecode(topic),unidecode(o.specialization))*2.5/10
							if(ratio>=75):
								details={}
								details['id']=str(o.p_id)
								details['name']=str(o.name)
								details['emailid']=str(o.emailid)
								details['specialization']=str(o.specialization)
								details['image']=str(o.image)
								response_json['prof_details'].append(details)
					else:	
						for o in prof_data.objects.filter(city=city):
							ratio=fuzz.partial_token_sort_ratio(unidecode(topic),unidecode(o.specialization))*7.5/10+fuzz.token_sort_ratio(unidecode(topic),unidecode(o.specialization))*2.5/10
							if(ratio>=75):
								details={}
								details['id']=str(o.p_id)
								details['name']=str(o.name)
								details['emailid']=str(o.emailid)
								details['specialization']=str(o.specialization)
								details['image']=str(o.image)
								response_json['prof_details'].append(details)
				else:
					for o in prof_data.objects.all():
						details={}
						details['id']=str(o.p_id)
						details['name']=str(o.name)
						details['emailid']=str(o.emailid)
						details['specialization']=str(o.specialization)
						details['image']=str(o.image)
						response_json['prof_details'].append(details)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']="Error in professor list"
				return JsonResponse(response_json)			
##################################################################################
		elif(type1==3):
			response_json['city_list']=[]
			try:
				for o in incubators_data.objects.filter(city=o.city):
					temp={}
					temp['city']=o.city
					response_json['city_list'].append(temp)
			except Exception,e:
				temp={}
				temp['city']='unavailable'
				response_json['city_list'].append(temp)
			try:
				response_json['incubator_details']=[]
				if(flag==1):
					for o in incubators_data.objects.filter(city=city):
						temp={}
						temp['id']=o.incubator_id
						temp['name']=o.name
						temp['website']=o.website
						temp['area']=o.thrust_area
						temp['city']=o.city
						response_json['incubator_details'].append(temp)
				elif(flag==2):
					for o in incubators_data.objects.all():
						ratio=fuzz.partial_token_sort_ratio(unidecode(topic),unidecode(o.thrust_area))*7.5/10+fuzz.token_sort_ratio(unidecode(topic),unidecode(o.thrust_area))*2.5/10
						if(ratio>=75):
							temp={}
							temp['id']=o.incubator_id
							temp['name']=o.name
							temp['website']=o.website
							temp['area']=o.thrust_area
							temp['city']=o.city
							response_json['incubator_details'].append(temp)
				elif(flag==3):
					for o in incubators_data.objects.filter(city=city):
						ratio=fuzz.partial_token_sort_ratio(unidecode(topic),unidecode(o.thrust_area))*7.5/10+fuzz.token_sort_ratio(unidecode(topic),unidecode(o.thrust_area))*2.5/10
						if(ratio>=75):
							temp={}
							temp['id']=o.incubator_id
							temp['name']=o.name
							temp['website']=o.website
							temp['area']=o.thrust_area
							temp['city']=o.city
							response_json['incubator_details'].append(temp)
				else:
					for o in incubators_data.objects.all():
						temp={}
						temp['id']=o.incubator_id
						temp['name']=o.name
						temp['website']=o.website
						temp['area']=o.thrust_area
						temp['city']=o.city
						response_json['incubator_details'].append(temp)	

			except Exception,e:
				print e
				print 'error in incubator data'
				response_json['success']=False
				response_json['message']='error in incubator data'

	return JsonResponse(response_json)

def city(request):
	type1=request.GET.get('type')
	response_json={}
	response_json['success']=True
	if(type1==0):
		city_list=prof_data.objects.values('city').distinct()
		response_json['city_list']=[]
		for o in city_list:
			temp={}
			temp['city']=str(o['data'])
		response_json['city_list']=temp
	else:
		response_json['success']=True
		response_json['message']="some error in type field"	
	return JsonResponse(response_json)



		
				





	







