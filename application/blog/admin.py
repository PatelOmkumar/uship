from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import blog
# Register your models here.

@admin.register(blog)
class blog(ImportExportModelAdmin):
    list_display = ['blog_name','blog_title','blog_pics','blog_desc','blog_date','isActive']
    search_fields=['blog_name','blog_title']
    list_filter=['blog_date','isActive']