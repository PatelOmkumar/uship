from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import User_TB,User

# Register your models here.

@admin.register(User_TB)
class UserView(ImportExportModelAdmin):
    list_display = ['gender','phone','address','profile_pic']
    #search_fields=['first_name','last_name','area_name']
    list_filter=['gender']


admin.site.register(User)