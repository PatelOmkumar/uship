from django.db import models

# Create your models here.

class ContactUs_TB(models.Model):
    First_name = models.CharField('First Name:',max_length=30)
    Last_name = models.CharField('Last Name:',max_length=30)
    Email = models.EmailField("Email ID:")
    Subject = models.CharField('Subject:',max_length=150)
    Mesg = models.TextField("Message:")
    Date=models.DateTimeField("Contact Date:",auto_now_add=True)
    class Meta:
        verbose_name  = "Contact U"