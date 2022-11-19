from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import bid
# Register your models here.

@admin.register(bid)
class Bidingview(ImportExportModelAdmin):
    list_display = ['bidding_date','price','company_name','max_price']
    search_fields = ['price','company_name']
    list_filter=['bidding_date','max_price']







