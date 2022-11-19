from django.db import models

# Create your models here.
class Complaints_TB(models.Model):
    complaint_text=models.CharField("Complaint Text:",max_length=250)
    Userid = models.ForeignKey("dbmodels.User_TB",on_delete=models.CASCADE)
    company_name=models.ForeignKey("company.Company_TB",on_delete=models.CASCADE)
    complaint_date=models.DateTimeField("Complaint Date:",auto_now_add=True)
    isActive=models.BooleanField(default=True)

    class Meta:
        verbose_name  = "User Complaint"