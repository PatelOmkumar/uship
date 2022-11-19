from django.db import models

# Create your models here.
class bid(models.Model):
    PostId = models.ForeignKey("post.post",on_delete=models.CASCADE,verbose_name="Post Id")
    bidding_date=models.DateTimeField("Bidding Date:",auto_now_add=True)
    price=models.DecimalField("Bidding Price:",max_digits=7,decimal_places=3)
    company_name=models.ForeignKey("company.Company_TB",on_delete=models.CASCADE)
    # bidding_desc=models.TextField("Bidding Description:")
    max_price = models.TextField("Base Price",blank=True,default='')
    
    class Meta:
        verbose_name  = "Bidding"