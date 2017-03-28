from django.contrib import admin
from .models import *

class user_datasModelAdmin(admin.ModelAdmin):
	list_display=["p_id","otp","flag","image","name","designation","city","phone","emailid","specialization","affliation","edu_degree","edu_institute","papers"]

	class Meta:
		model=prof_data

admin.site.register(prof_data,user_datasModelAdmin)

class student_dataModelAdmin(admin.ModelAdmin):
	list_display=["student_id","name","emailid","institution","skills","place","current_year","degree","experience","resume","image"]

	class Meta:
		model=student_data

admin.site.register(student_data,student_dataModelAdmin)

class project_dataModelAdmin(admin.ModelAdmin):
	list_display=["project_id","student_id","title","description","date","field","modified","created"]

	class Meta:
		model=projects

admin.site.register(projects,project_dataModelAdmin)
# Register your models here.


# Register your models here.
