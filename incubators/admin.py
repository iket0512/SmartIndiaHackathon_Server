from django.contrib import admin
from .models import *

class incubator_datasModelAdmin(admin.ModelAdmin):
	list_display=["incubator_id","name","state","facilities","city","thrust_area","address","contact_name","contact_designation","contact_email","contact_phone"]

	class Meta:
		model=incubators_data

admin.site.register(incubators_data,incubator_datasModelAdmin)
# Register your models here.
