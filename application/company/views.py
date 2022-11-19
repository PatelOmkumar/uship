from django.shortcuts import render,redirect
from .forms import CompanyForms
from .models import Company_TB
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from category.models import Category
from booking.models import *

# Create your views here.

# '''def index(request):
#     if request.method == "POST":
#         forms = CompanyForms(request.POST or None , request.FILES or None)
#         if forms.is_valid():
#             forms.save()
#         else:
#             forms = CompanyForms()
#     return render(request,"company/index.html",{'forms':forms,'msg':"Thank You For Registering"})'''

# def index(request):
#     forms = CompanyForms(request.POST,request.FILES)
#     if request.method == "POST":
#           if forms.is_valid():
#                forms.save()
#                return redirect('CompanySignup')
#           else:
#                print("error while inserting data")
#     return render(request,"company/index.html",{'forms':forms})

def loginpage(request):
     if request.method == "POST":
          companyname = request.POST['username']
          password = request.POST['pwd']
          company = authenticate(request,username = companyname, password=password)
          if company is not None:
               if company.is_active and company.is_company:
                    login(request, company)
                    return redirect('/')
          return render(request,"company/login.html",{'inactivemsg':"Invalid Companyname Or Password"})
     return render(request,"company/login.html",{'msg':"Invalid Companyname Or Password"})


def companylogout(request):
  logout(request)
  return render(request,"main.html")


def myaccount(request):
  return render(request,"company/myaccount.html")

def companybooking(request):
  listbook = Booking.objects.filter(Userid=request.user)
  context = {
    'listbook':listbook
  }
  return render(request,"company/companybookin.html",context)


def companycate(request,id):
     category_id = Category.objects.get(pk=id)
     company_list = Company_TB.objects.filter(company_category=category_id,isActive=True)
     return render(request,"companylist.html",{'company_list':company_list})

def CompanyView(request,id):
    company_view = Company_TB.objects.filter(id=id,isActive=True)
    return render(request,"company/companyview.html",{'company_view':company_view})
