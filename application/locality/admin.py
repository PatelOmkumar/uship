from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import state,city,area

# Register your models here.

@admin.register(state)
class StateView(ImportExportModelAdmin):
    list_display = ['state_name','insert_date','isActive']
    search_fields=['state_name']
    list_filter=['isActive']

@admin.register(city)
class CityView(ImportExportModelAdmin):
    list_display = ['state_name','city_name','insert_date','isActive']
    search_fields=['state_name','city_name']
    list_filter=['isActive']

@admin.register(area)
class AreaView(ImportExportModelAdmin):
    list_display = ['city_name','area_name','pincode','insert_date','isActive']
    search_fields=['city_name','area_name']
    list_filter=['isActive']
