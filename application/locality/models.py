from django.db import models

# Create your models here.
class state(models.Model):
    state_name=models.CharField("State Name:",max_length=20)
    insert_date=models.DateTimeField("Insert Date:",auto_now_add=True)
    isActive=models.BooleanField(default="True")
    def __str__(self):
        return self.state_name

class city(models.Model):
    state_name=models.ForeignKey("state",on_delete=models.CASCADE)
    city_name=models.CharField("City Name:",max_length=20)
    insert_date=models.DateTimeField("Insert Date:",auto_now_add=True)
    isActive=models.BooleanField(default="True")

    def __str__(self):
        return self.city_name

class area(models.Model):
    city_name=models.ForeignKey("city",on_delete=models.CASCADE)
    area_name=models.CharField("Area Name:",max_length=20)
    pincode=models.IntegerField("Pincode:")
    insert_date=models.DateTimeField("Insert Date:",auto_now=True)
    isActive=models.BooleanField(default="True")
    def __str__(self):
        return self.area_name