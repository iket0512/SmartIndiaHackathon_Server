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
	search_keyword=request.GET.get('keyword')
	response_json={}
	prof_list=[]
	project_list=[]
	if(request.method=='GET'):
		response_json['success']=True
		response_json['message']='Successful'
		try:
			for o in prof_data.objects.all():
				ratio=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.name))*2.5/10
				ratio1=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.specialization))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.specialization))*2.5/10
				ratio2=fuzz.partial_token_sort_ratio(unidecode(search_keyword),unidecode(o.papers))*7.5/10+fuzz.token_sort_ratio(unidecode(search_keyword),unidecode(o.papers))*2.5/10
				print "percentage_matched","ab",o.data,ratio
				if(ratio1>=70 or ratio>=70 or ratio2>=70):
					detail={}
					detail['id']=str(o.pid)
					detail['name']=str(o.name)
					detail['speciality']=str(o.specialization)
					prof_list.append(detail)
					# prof_list['type']=1
			response_json['prof_list']=prof_list
		except Exception,e:
			print e
		response_json['projects']=project_list
	else:
		response_json['success']=False
		response_json['message']="not get method"
	print str(response_json)
	return JsonResponse(response_json)
# Create your views here.
