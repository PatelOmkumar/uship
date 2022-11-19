from django.db import models

# Create your models here.
class Booking(models.Model):
    Userid = models.ForeignKey("dbmodels.User",on_delete=models.CASCADE,verbose_name="User Name")
    company_name = models.ForeignKey("company.Company_TB",null=True,blank=True,on_delete=models.CASCADE,verbose_name="Company Name")
    mes = models.TextField("Message",blank=True,default='')
    phone_number = models.CharField("Phone Number",max_length=150)
    altphone_number = models.CharField("Phone Number",max_length=150,blank=True)
    from_place = models.CharField("From",max_length=150,blank=True)
    To_place = models.CharField("To",max_length=150,blank=True)
    category_id = models.ForeignKey("category.Category",on_delete=models.CASCADE,verbose_name="Category Name")
    moving_date = models.DateTimeField("Moving Date")
    #subcate = models.ForeignKey("category.Subcategory",on_delete=models.CASCADE,verbose_name="Sub Category Name")

    def __str__(self):
        return self.mes

    



