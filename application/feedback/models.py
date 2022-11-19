from django.db import models

# Create your models here.
class feedback_TB(models.Model):
    #user id and admin id as a foreign key
    # First_name = models.CharField('First Name:',max_length=30)
    # Last_name = models.CharField('Last Name:',max_length=30)
    # Email = models.EmailField('Email ID:')
    # Subject = models.CharField('Subject:',max_length=150)
    Userid = models.ForeignKey("dbmodels.User_TB",on_delete=models.CASCADE)
    Mesg = models.TextField('Message:')
    Feedback_date=models.DateTimeField("Feedback Date:",auto_now_add=True)
    
    class Meta:
        verbose_name  = "System FeedBack"