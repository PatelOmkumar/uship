from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Valet_Details_TB

# Register your models here.

@admin.register(Valet_Details_TB)
class ValetView(ImportExportModelAdmin):
    list_display = ['valet_fname','valet_lname','company_name','valet_desc','phone','profile_pic','gender']
    search_fields=['valet_fname','valet_lname','company_name']
    list_filter=['gender']