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
		search_keyword=request.GET.get('query')
		type_data=request.GET.get('type')
	except Exception,e:
		response_json['success']=False
		response_json['message']='Error in receiving search keyword and type'
		return response_json
	if(request.method=='GET'):
		if(type_data=='1'):
			try:
				response_json['equipment_list']=[]
				for o in equipment_data.objects.all():
					ratio=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*2.5/10
					ratio1=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.description))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.description))*2.5/10
					ratio2=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.features))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.features))*2.5/10
					if(ratio1>=70 or ratio>=70 or ratio2>=70):
						detail={}
						detail['id']=str(o.equipment_id)
						detail['name']=str(o.name)
						detail['image']=str(o.photo)
						detail['features']=str(o.features)
						detail['city']=str(o.city)
						response_json['equipment_list'].append(detail)
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']='error in Equipments data'
				return JsonResponse(response_json)

		elif(type_data=='2'):
			try:
				response_json['incubator_list']=[]
				for o in incubator_data.objects.all():
					ratio=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*2.5/10
					ratio1=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.facilities))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.facilities))*2.5/10
					ratio2=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.thrust_area))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.thrust_area))*2.5/10
					if(ratio1>=70 or ratio>=70 or ratio2>=70):
						detail={}
						detail['id']=str(o.incubator_id)
						detail['name']=str(o.name)
						detail['image']=str(o.image)
						detail['website']=str(o.website)
						detail['city']=str(o.city)
						response_json['incubator_list'].append(detail)
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']='error in incubator data'
				return JsonResponse(response_json)

		elif(type_data=='3'):
			try:
				response_json['incubator_list']=[]
				for o in biotech_data.objects.all():
					ratio=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*2.5/10
					ratio1=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.facilities))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.facilities))*2.5/10
					if(ratio1>=70 or ratio>=70):
						detail={}
						detail['id']=str(o.biotech_id)
						detail['name']=str(o.name)
						detail['image']=str(o.image)
						detail['website']=str(o.website)
						detail['city']=str(o.city)
						response_json['incubator_list'].append(detail)
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']='error in biotech data'
				return JsonResponse(response_json)

		elif(type_data=='4'):
			try:
				response_json['incubator_list']=[]
				for o in prof_data.objects.all():
					ratio=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*2.5/10
					ratio1=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.facilities))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.facilities))*2.5/10
					if(ratio1>=70 or ratio>=70):
						detail={}
						detail['id']=str(o.p_id)
						detail['name']=str(o.name)
						detail['image']=str(o.image)
						detail['website']=str(o.website)
						detail['city']=str(o.city)
						response_json['incubator_list'].append(detail)
						# prof_list['type']=1
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']='error in prof_data search'
				return JsonResponse(response_json)

		elif(type_data=='5'):
			response_json['article_list']=[]
			response_json['success']=True
			response_json['message']='Pubmed Data'
			json={}
			print search_keyword
			try:
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
			except Exception,e:
				response_json['success']=False
				response_json['message']='some error in pubmed api'
			return JsonResponse(response_json)

		elif(type_data=='6'):
			try:
				response_json['survey_list']=[]
				for o in survey_data.objects.all():
					ratio=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.title))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.title))*2.5/10
					ratio1=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.field))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.field))*2.5/10
					ratio2=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.description))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.description))*2.5/10
					if(ratio1>=70 or ratio>=70 or ratio2>=70):
						detail={}
						detail['id']=str(o.survey_id)
						detail['field']=str(o.field)
						detail['title']=str(o.title)
						detail['description']=str(o.description)
						response_json['survey_list'].append(detail)
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']='error in survey_data search'
				return JsonResponse(response_json)

		elif(type_data=='7'):
			try:
				response_json['user_list']=[]
				for o in student_data.objects.filter(type1=1):
					ratio=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.institution))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.institution))*2.5/10
					ratio1=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*2.5/10
					ratio2=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.specialization))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.specialization))*2.5/10
					ratio3=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.skills))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.skills))*2.5/10
					if(ratio1>=70 or ratio>=70 or ratio2>=70 or ratio3>=70):
						detail={}
						detail['id']=str(o.student_id)
						detail['name']=str(o.field)
						detail['emailid']=str(o.title)
						detail['specialization']=str(o.description)
						detail['skills']=str(o.skills)
						response_json['user_list'].append(detail)
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']='error in survey_data search'
				return JsonResponse(response_json)

		elif(type_data=='8'):
			try:
				response_json['user_list']=[]
				for o in student_data.objects.filter(type1=0):
					ratio=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.institution))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.institution))*2.5/10
					ratio1=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*2.5/10
					ratio2=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.specialization))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.specialization))*2.5/10
					ratio3=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.skills))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.skills))*2.5/10
					if(ratio1>=70 or ratio>=70 or ratio2>=70 or ratio3>=70):
						detail={}
						detail['id']=str(o.student_id)
						detail['name']=str(o.field)
						detail['emailid']=str(o.title)
						detail['specialization']=str(o.description)
						detail['skills']=str(o.skills)
						response_json['user_list'].append(detail)
				response_json['success']=True
				return JsonResponse(response_json)
			except Exception,e:
				print e
				response_json['success']=False
				response_json['message']='error in survey_data search'
				return JsonResponse(response_json)		

TITLE='Equipments|Incubators|Biotech Parks|Institution|Articles|Surveys|Professors|Students'
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