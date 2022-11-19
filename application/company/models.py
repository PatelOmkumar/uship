from django.db import models
# from django.authenticate import password_hash

# Create your models here.
class Company_TB(models.Model):
    company_name=models.CharField("Company Name:",max_length=100)
    company_phone=models.CharField("Company Phone:",max_length = 11)
    company_password=models.CharField("Password:",max_length=20)
    company_cpassword=models.CharField("Confirm Password:",max_length=20)
    company_address=models.TextField("Company Address:")
    company_emailid=models.EmailField("Company Email ID:",unique=True)
    company_logo=models.ImageField("Company Logo:",upload_to="companylogoimages/")
    company_desc=models.TextField("Company Description:")
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
