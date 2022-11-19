from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
#from multiupload.fields import MultiFileField
# Create your models here.
class post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #user = models.CharField(max_length=150)
    post_img = models.FileField("Post Image:",upload_to="postimages/")
    post_desc = models.TextField("Post Description:",max_length=500)
    post_price = models.IntegerField("Estimated Price: ")
    #category_name = models.ForeignKey("category.Category",null=True,on_delete=models.CASCADE,blank=True,default='')
    scrap_kg = models.IntegerField("Estimated Scrap in Kg:")
    #subcate_name = models.ForeignKey("category.Subcategory",on_delete=models.CASCADE)
    isActive=models.BooleanField(default=False)