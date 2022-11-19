from django.db import models

# Create your models here.
class Valet_Details_TB(models.Model):
    valet_fname=models.CharField(max_length=20)
    valet_lname=models.CharField(max_length=20)
    company_name=models.ForeignKey("company.Company_TB",on_delete=models.CASCADE)
    valet_desc=models.CharField(max_length=1000)
    phone=models.IntegerField()
    profile_pic=models.ImageField(upload_to="valetprofilepicimages/",default="",blank=True)
    gender=models.CharField(max_length=1,
    choices=(
        ('M','Male'),
        ('F','Female')
    ))

    class Meta:
        verbose_name  = "Valet"