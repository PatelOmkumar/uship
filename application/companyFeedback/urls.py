from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index,name="CompanySignup"),
    path('',views.index,name="mainpage"),
   

]
