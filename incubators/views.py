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
		# access=
# Create your views here.
