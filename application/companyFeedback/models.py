from django.db import models

# Create your models here.
class companyFeedback_TB(models.Model):
    Userid = models.ForeignKey("dbmodels.User_TB",null=True,on_delete=models.CASCADE)
    Mesg = models.TextField('Message:')
    Feedback_date=models.DateTimeField("Feedback Date:",auto_now_add=True)
    
    class Meta:
        verbose_name  = "Company FeedBack"