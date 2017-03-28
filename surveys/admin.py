from django.contrib import admin
from .models import *

class surveyModelAdmin(admin.ModelAdmin):
	list_display=['survey_id','access_token','user_type','title','description','question1','question2','question3','question4','created','modified']

	class Meta:
		model=survey_data

admin.site.register(survey_data,surveyModelAdmin)
# Register your models here.
