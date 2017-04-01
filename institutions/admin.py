from django.contrib import admin
from .models import *
# Register your models here.
class institute_datasModelAdmin(admin.ModelAdmin):
	list_display=["institute_id","name","city","address"]

	class Meta:
		model=institute_data

admin.site.register(institute_data,institute_datasModelAdmin)
