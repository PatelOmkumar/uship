from django.db import models
from .validators import validate_file_extension
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
#from locality.models import state

#state.get_model('state', 'state')

class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

    first_name = models.CharField("First Name:",max_length=15)
    last_name = models.CharField("Last Name:",max_length=15)
    


# Create your models here.
class User_TB(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    gender=models.CharField("Gender:",max_length=1,
    choices=(
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ),default="M")
    phone=models.CharField("Phone No:",max_length=11)
    address=models.TextField("Address:")
    profile_pic=models.ImageField(upload_to="userprofilepicimages",validators=[validate_file_extension])
    

class Company_table(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    company_logo=models.ImageField("Company Logo:",upload_to="companylogoimages/")
    company_desc=models.TextField("Company Description:",default="",null=True)
    city = models.ManyToManyField("locality.city")
    state = models.ManyToManyField("locality.state")
    branch = models.ManyToManyField("locality.area")
    company_category = models.ForeignKey("category.Category",on_delete=models.SET_NULL,null=True)
    company_work  = models.CharField("Company Work:",max_length = 4, choices = (
        ('P',"Packing"),
        ('M',"Moving"),
        ('PM',"Both Packing and Moving"),
        ('SC',"Scrap Collectors"),
        ('PMSC',"Both Packing and Moving with Scrap Collectors"),
    ))
    #company_subcategory = models.ForeignKey("category.Subcategory",on_delete=models.SET_NULL,null=True)
    isActive=models.BooleanField(default=False)
    #2 more foreign key fields that is from category and locality
    
    class Meta:
        verbose_name  = "Company Register"
    
    
