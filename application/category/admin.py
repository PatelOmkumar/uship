from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Category

# Register your models here.

@admin.register(Category)
class CategoryView(ImportExportModelAdmin):
    list_display = ['category_name','status','Dateandtime']
    search_fields = ['category_name']
    list_filter=['status','Dateandtime']

# @admin.register(Subcategory)
# class SubCategoryView(ImportExportModelAdmin):
#     list_display = ['category_name','subcate_name','status','dateandtime']
#     search_fields = ['subcate_name']
#     list_filter=['status','dateandtime']