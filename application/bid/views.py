from django.shortcuts import render
from .forms import BidForms
from .models import bid
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    objec = bid.objects.all()
    return render(request,"bid/index.html",{'objec':objec})

def post(request):
    objec = bid.objects.all()
    return render(request,"post/index.html",{'objec':objec})


@login_required(login_url='companylogin')
def companybid(request):
	objec = BidForms(request.POST)
	if objec.is_valid():
		objec.save()
		return redirect('viewallpost')
	context = {
	'objec':objec
	}
	return render(request,"bid/userbid.html",context)