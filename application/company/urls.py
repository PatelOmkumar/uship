from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index,name="CompanySignup"),
    path('companycate/<int:id>/',views.companycate,name="companycate"),
    path('CompanyView/<int:id>/',views.CompanyView,name="CompanyView"),
    path('loginpage/',views.loginpage,name="companylogin"),
    path('companylogout/',views.companylogout,name="companylogout"),
    path('myaccount/',views.myaccount,name="companyaccount"),
    path('companybooking/',views.companybooking,name="companybooking")

]
