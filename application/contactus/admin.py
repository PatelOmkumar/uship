from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import ContactUs_TB

# Register your models here.

@admin.register(ContactUs_TB)
class ContactUsView(ImportExportModelAdmin):
    list_display = ['First_name','Last_name','Email','Subject','Mesg','Date']   
    search_fields=['First_name','Last_name','Email']
    list_filter=['Date']