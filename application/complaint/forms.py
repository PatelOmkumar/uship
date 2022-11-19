from django import forms
from .models import Complaints_TB

class ComplaintForms(forms.ModelForm):
    class Meta:
        model = Complaints_TB
        fields = '__all__'
