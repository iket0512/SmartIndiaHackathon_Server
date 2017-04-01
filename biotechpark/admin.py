from django.contrib import admin
from .models import biotech_data
# Register your models here.

class biotech_datasModelAdmin(admin.ModelAdmin):
	list_display=["biotech_id","name","city","facilities","address","website","contact_name","contact_designation","contact_email","contact_phone"]

	class Meta:
		model=biotech_data

admin.site.register(biotech_data,biotech_datasModelAdmin)

