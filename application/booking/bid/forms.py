from django import forms
from .models import bid

class BidForms(forms.ModelForm):
    class Meta:
        model = bid
        fields = '__all__'
