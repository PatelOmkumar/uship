from django.shortcuts import render,redirect
from .forms import PostForms
from .models import post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

@login_required(login_url='loginpage')
def index(request):
    forms = PostForms(request.POST, request.FILES)
    #user = User.objects.filter(username = request.session['user'])
    if request.method == "POST":

        if forms.is_valid():
            profile = forms.save(commit=False)
            profile.user = request.user
            forms.cleaned_data['post_img']
            profile.save()
            return redirect('myaccount')
        else:
            print("error while inserting data")
    return render(request,"post/index.html",{'forms':forms})


def viewallpost(request):
    postlist = post.objects.filter(isActive=True)
    context = {
        'postlist':postlist
    }
    return render(request,"post/viewallpost.html",context)