from django import forms
from .models import feedback_TB

class FeedbackForms(forms.ModelForm):
    class Meta:
        model = feedback_TB
        fields = '__all__'
