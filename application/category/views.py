from django.shortcuts import render
from .models import Category

# Create your views here.
def category(request):
     cate = Category.objects.filter(status=True)
     return render(request,"allcategory.html",{'cate':cate})