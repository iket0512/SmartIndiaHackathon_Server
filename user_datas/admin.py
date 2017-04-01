from django.contrib import admin
from .models import *

class user_datasModelAdmin(admin.ModelAdmin):
	list_display=["p_id","otp","flag","image","name","city","phone","emailid"]

	class Meta:
		model=prof_data

admin.site.register(prof_data,user_datasModelAdmin)

class student_dataModelAdmin(admin.ModelAdmin):
	list_display=["student_id","name","emailid","institution","skills","city","degree","experience","resume","image"]

	class Meta:
		model=student_data

admin.site.register(student_data,student_dataModelAdmin)

# Register your models here.


# Register your models here.
