from django.contrib import admin
from .models import *

class equipment_datasModelAdmin(admin.ModelAdmin):
	list_display=["equipment_id","name","institute"]

	class Meta:
		model=equipment_data

admin.site.register(equipment_data,equipment_datasModelAdmin)
# Register your models here.
