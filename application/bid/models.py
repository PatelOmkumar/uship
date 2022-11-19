from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class bid(models.Model):
	user = models.ForeignKey(User,null=True,on_delete=models.CASCADE) 
	PostId = models.ForeignKey("post.post",null=True,on_delete=models.CASCADE,verbose_name="Post Id")
	bidding_date=models.DateTimeField("Bidding Date:",auto_now_add=True)
	price = models.DecimalField("Bidding Price:",max_digits=7,decimal_places=3)
	max_price = models.TextField("Base Price",blank=True,default='')

	class Meta:
		verbose_name  = "Bidding"