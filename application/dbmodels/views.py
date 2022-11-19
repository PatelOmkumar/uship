from django.shortcuts import render,redirect
from .forms import UserForms,CompanyForms,companyFeedbackForm
from .models import User_TB,User
#from django.contrib.auth.forms import UserForms
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.views.generic import CreateView
#from django.url import reverse_lazy
from django.views import generic
from post.models import post
from django.urls import path
from django.urls import reverse_lazy
from companyFeedback.models import companyFeedback_TB


# Create your views here.
def home(request):
    return render(request,"main.html",)

def faq(request):
     return render(request,"faq.html")

def howitworks(request):
     return render(request,"howitworks.html")

def about(request):
    return render(request,"about.html")

def packersandmovers(request):
     return render(request,"packersandmovers.html")

def scrapcollectors(request):
     return render(request,"scrapcollectors.html")

def bothpackersandmovers(request):
     return render(request,"bothpackersandmovers.html")

def loginpage(request):
     if request.method == "POST":
          username = request.POST['username']
          password = request.POST['pwd']
          user = authenticate(request,username = username, password=password)
          if user is not None:
               if user.is_user and user.is_active:
                    request.session['user'] = username
                    login(request, user)
                    return redirect('/')
          return render(request,"dbmodels/login.html",{'inactivemsg':"Invalid Username Or Password"})
     return render(request,"dbmodels/login.html",{'msg':"Invalid Username Or Password"})

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('loginpage')



class UserForm(CreateView):
    model = User
    form_class = UserForms
    template_name = 'dbmodels/signup.html'

    # def get_context_data(self,**kwargs):
    #     kwargs['user_type'] = 'SimpleUser'
    #     return super().get_context_data(**kwargs)

    # def form_valid(self,form):
    #     user = form.save()
    #     login(self.request,user)
    #     return redirect('loginpage')


class CompanyForm(CreateView):
    model = User
    form_class = CompanyForms
    template_name = 'company/index.html'
    
    def get_context_data(self,**kwargs):
        kwargs['user_type'] = 'CompanyUser'
        return super().get_context_data(**kwargs)    

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return redirect('companylogin')



@login_required(login_url='loginpage')
def myaccount(request):
    forms = UserForms(request.POST,request.FILES,instance=request.user)
    if forms.is_valid():
        forms.save()
        print("Your Profile Has Been Updated")
    else:
        print("My account Error")    
    return render(request=request, template_name="dbmodels/myaccount.html", context={"user":request.user,"forms":forms })
     
def logout_view(request):
     logout(request)
     return render(request,"main.html")
    
@login_required(login_url='loginpage')
def mypost(request):
    obje = post.objects.filter(isActive=True,user=request.user)
    context = {
        'obje':obje
    }
    return render(request,"dbmodels/mypost.html",context)

def forgotpassword(request):
     forms  = UserForms(request.POST,request.FILES)
     return render(request,"dbmodels/forgotpassword.html",{'forms':forms})

def mybookings(request):
     return render(request,"dbmodels/MyBookings.html")


def companyFeedback(request):
    forms = companyFeedbackForm(request.POST)
    if forms.is_valid():
        forms.save()
    else:
        print('error companyfeedback')
    return render(request,"dbmodels/companyFeedback.html",{'forms':forms})

def companycomplaint(request):
     return render(request,"dbmodels/companycomplaint.html")

def bidlist(request):
     return render(request,"dbmodels/bidlist.html")
