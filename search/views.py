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
		# type_data='5'
		# search_keyword='breast cancer'
		search_keyword=request.GET.get('query')
		type_data=request.GET.get('type')
	except Exception,e:
		response_json['success']=False
		response_json['message']='Error in receiving search keyword and type'
		return response_json	
	if(request.method=='GET'):
		if(type_data=='0'):
			try:
				response_json['product_list']=[]
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
						response_json['product_list'].append(detail)
						# prof_list['type']=1
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']='error in prof_data search'
				return JsonResponse(response_json)
		elif(type_data=='2'):
			try:
				response_json['product_list']=[]
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
						response_json['product_list'].append(detail)
						# prof_list['type']=1
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']='error in prof_data search'
				return JsonResponse(response_json)		
		elif(type_data=='1'):
			response_json['article_list']=[]
			response_json['success']=True
			response_json['message']='Pubmed Data'
			json={}
			print search_keyword
			url=str("http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmax=8&term="+search_keyword+"&retmode=json")
			response=requests.get(url)
			json=response.json()

			json1=json['esearchresult']['idlist']
			print json1
			url1=str("http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&rettype=abstract&id=")
			for o in json1:
				url1=url1+str(o)+","
			print url1
			response1=requests.get(url1)
			json=response1.json()
			json2=json['result']
			print '################################'
			for o in json2['uids']:
				detail={}					
				detail['uid']=json2[o]['uid']
				detail['pubdate']=json2[o]['pubdate']
				detail['source']=json2[o]['source']
				detail['title']=json2[o]['title']
				response_json['article_list'].append(detail)		
			return JsonResponse(response_json)


TITLE='Professors|Students|Surveys|Incubators|Equipments|Articles|Institution|Biotech Parks'
def tab_titles(request):
	json_response={}
	json_response['success']=True
	json_response['message']='Titles received'
	json_response['sub_category_list']=[]
	if(request.method=='GET'):
		try:
			i=1
			for o in TITLE.split('|'):
				temp={}
				temp['name']=o
				temp['sub_category_id']=str(i)
				i=i+1
				json_response['sub_category_list'].append(temp)
		except Exception,e:
			print e
			json_response['success']=False
			json_response['message']='titles not received'
			json_response['message_error']=str(e)
	print json_response	
	return JsonResponse(json_response)	

# # Create your views here.
# 			json_response['sub_category_list']=[]
# 			temp={}
# 			temp['id']='0'
# 			temp['title']='Proffesors'
# 			json_response['tabs'].append(temp)
# 			temp={}
# 			temp['id']='1'
# 			temp['title']='Students'
# 			json_response['tabs'].append(temp)
# 			temp={}
# 			temp['id']='2'
# 			temp['title']='Surveys'
# 			json_response['tabs'].append(temp)
# 			temp={}
# 			temp['id']='3'
# 			temp['title']='Incubators'
# 			json_response['tabs'].append(temp)
# 			temp={}
# 			temp['id']='4'
# 			temp['title']='Equipments'
# 			json_response['tabs'].append(temp)
# 			temp={}
# 			temp['id']='5'
# 			temp['title']='Articles'
# 			json_response['tabs'].append(temp)
# 			temp={}
# 			temp['id']='6'
# 			temp['title']='Institution'
# 			json_response['tabs'].append(temp)
# 			temp={}
# 			temp['id']='7'
# 			temp['title']='Biotech Parks'
# 			json_response['tabs'].append(temp)
# # 