from django.shortcuts import render
from .forms import BlogForms
from .models import blog

# Create your views here.
def index(request):
    objec = blog.objects.all()
    return render(request,"blog/index.html",{'objec':objec})

