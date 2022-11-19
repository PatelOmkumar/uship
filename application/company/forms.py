from django import forms
from django.forms import ModelForm
from .models import Company_TB

class CompanyForms(forms.ModelForm):
    class Meta:
        model = Company_TB
        fields = ('company_name','company_phone','company_password','company_cpassword','company_address','company_emailid','company_logo','company_desc','company_category','company_work','city','state')
        widgets = {
            'company_name':forms.TextInput(attrs={'class':'text-input','title':'Enter Your Company Name','id':'company_name'}),
            'company_phone':forms.TextInput(attrs={'class':'text-input','title':'Enter Your 10 digits Company Contact Information','id':'company_phone'}),
            'company_password':forms.PasswordInput(attrs={'class':'text-input','title':'Minimum 8 characters\nAtleast 1 UPPERCASE letter\nAtleast 1 lowercase letter\nAtleast 1 Special character\nMust Contain Numbers\nMaximum 20 characters\n\nFor Example:Xaviers@123','id':'company_password'}),
            'company_cpassword':forms.PasswordInput(attrs={'class':'text-input','title':'Confirm your password here','id':'company_cpassword'}),
            'company_address':forms.Textarea(attrs={'class':'text-input','title':'Enter your street details\n\nFor example: 202, Heritage Horizon,Nr. Bawarchi Rest. Off','id':'company_address'}),
            'company_emailid':forms.EmailInput(attrs={'class':'text-input','title':'Provide Email ID with lower case\nMust contain @ and . symbols\n\nFor Example:sxca@edu.in','id':'company_emailid'}),
            'company_logo':forms.FileInput(attrs={'class':'text-input','title':'Choose your company logo','id':'company_logo'}),
            'company_desc':forms.Textarea(attrs={'class':'text-input','title':'Your Company About Information as your description','id':'company_desc'}),
            'company_category':forms.Select(attrs={'class':'text-input','title':'Choose your category','id':'company_category'}),
            'company_work':forms.Select(attrs={'class':'text-input','title':'Choose your work type','id':'company_work'}),
            'state':forms.SelectMultiple(attrs={'class':'text-input','title':'Select the states you work in','id':'state'}),
            'city':forms.SelectMultiple(attrs={'class':'text-input','title':'Select the cities you work in','id':'city'}),
            # 'branch':forms.SelectMultiple(attrs={'class':'text-input','title':'Select the areas of your branch\n\nFor Example:','id':'branch'}),
        }



    
        



