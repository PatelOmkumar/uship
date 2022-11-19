from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import feedback_TB

# Register your models here.

@admin.register(feedback_TB)
class FeedbackView(ImportExportModelAdmin):
    list_display = ['Mesg','Feedback_date']   
    # search_fields=['First_name','Last_name','Email']
    list_filter=['Feedback_date']