from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Complaints_TB

# Register your models here.

@admin.register(Complaints_TB)
class ComplaintView(ImportExportModelAdmin):
    list_display = ['complaint_text','Userid','company_name','complaint_date','isActive']
    search_fields = ['complaint_text','company_name']
    list_filter=['isActive','complaint_date']