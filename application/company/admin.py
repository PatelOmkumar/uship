from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Company_TB

# Register your models here.

@admin.register(Company_TB)
class CompanyView(ImportExportModelAdmin):
    list_display = ['company_name','company_phone','company_address','company_emailid','company_logo','company_desc','isActive','company_category']
    search_fields = ['company_name','company_category']
    list_filter=['isActive']