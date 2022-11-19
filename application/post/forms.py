from django import forms
from .models import post


from django.forms import ModelForm


class PostForms(forms.ModelForm):
    class Meta:
        model = post
        fields = ['post_img','post_desc','post_price','scrap_kg']
        exclude = ['user']
        widgets = {
            'post_desc':forms.Textarea(attrs={'class':'text-input','title':'Provide your post description here'}),
        }
