from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import requests
import operator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from equipment.models import equipment_data

def get_incubator(requests):
	if(request.method=='GET'):
		try:
			access=request.GET.get('id')
			response_json={}
			for o in incubator_data.objects.filter(incubator_id=access):
				response_json['name']=o.name
				response_json['state']=o.state
				response_json['city']=o.city
				response_jsonp['facilities']=o.facilities
				response_json['thrust_area']=o.thrust_area
				response_json['address']=o.address
				response_json['website']=o.website
				response_json['contact_person']=o.contact_person
				response_json['contact_phone']=o.contact_phone
				response_json['contact_email']=o.contact_email
				response_json['contact_designation']=o.contact_designation
				response_json['latitude']=o.latitude
				response_json['longitude']=o.longitude
				response_json['success']=True
		except Exception,e:
			response_json['success']=facilities
			response_json['message']='error'
	return JsonResponse(response_json)
# Create your views here.
