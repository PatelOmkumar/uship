from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import post

# Register your models here.

@admin.register(post)
class PostView(ImportExportModelAdmin):
    list_display = ['post_desc','post_img','scrap_kg','isActive']
    search_fields=['post_desc']
    list_filter=['isActive']