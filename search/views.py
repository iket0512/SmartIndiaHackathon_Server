from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import requests
import operator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import fuzzywuzzy.fuzz as fuzz
from unidecode import unidecode
from user_datas.models import *

@csrf_exempt
def search(request):
	fuzz.partial_token_sort_ratio
	response_json={}
	try:
		type_data='0'
		search_keyword='tuber'
		# search_keyword=request.GET.get('keyword')
		# type_data=request.GET.get('type')
	except Exception,e:
		response_json['success']=False
		response_json['message']='Error in receiving search keyword and type'
		return response_json	
	if(request.method=='GET'):
		if(type_data=='0'):
			try:
				response_json['prof_list']=[]
				for o in prof_data.objects.all():
					ratio=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*2.5/10
					ratio1=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.specialization))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.specialization))*2.5/10
					ratio2=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.papers))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.papers))*2.5/10
					if(ratio1>=70 or ratio>=70 or ratio2>=70):
						detail={}
						detail['id']=str(o.p_id)
						detail['name']=str(o.name)
						detail['speciality']=str(o.specialization)
						detail['college']=str(o.affliation)
						response_json['prof_list'].append(detail)
						# prof_list['type']=1
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']='error in prof_data search'
				return JsonResponse(response_json)		


def tab_titles(request):
	json_response={}
	json_response['success']=True
	json_response['message']='Titles received'
	try:
		if(request.method=='GET'):
			json_response['tabs']=[]
			temp={}
			temp['id']='0'
			temp['title']='Proffesors'
			json_response['tabs'].append(temp)
			temp={}
			temp['id']='1'
			temp['title']='Students'
			json_response['tabs'].append(temp)
			temp={}
			temp['id']='2'
			temp['title']='Surveys'
			json_response['tabs'].append(temp)
			temp={}
			temp['id']='3'
			temp['title']='Incubators'
			json_response['tabs'].append(temp)
			temp={}
			temp['id']='4'
			temp['title']='Equipments'
			json_response['tabs'].append(temp)
			temp={}
			temp['id']='5'
			temp['title']='Articles'
			json_response['tabs'].append(temp)
			temp={}
			temp['id']='6'
			temp['title']='Institution'
			json_response['tabs'].append(temp)
			temp={}
			temp['id']='7'
			temp['title']='Biotech Parks'
			json_response['tabs'].append(temp)
	except Exception,e:
		json_response['success']=False
		json_response['message']='titles not received'
			
	return JsonResponse(json_response)	

# Create your views here.
