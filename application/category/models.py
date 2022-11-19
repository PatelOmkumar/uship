from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    cate_des = models.TextField(default="")
    cate_img = models.ImageField(upload_to="cateimages/",default="")
    status = models.BooleanField(default=False)
    Dateandtime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.category_name

# class Subcategory(models.Model):
#     category_name =  models.ForeignKey("Category",on_delete=models.CASCADE)
#     subcate_name = models.CharField(max_length=50)
#     Subcate_des = models.TextField(default="")
#     SubCate_images = models.ImageField(upload_to = "Subcateimages",default="")
#     price = models.DecimalField(max_length=20,max_digits=3,decimal_places=2,default="")
#     status = models.BooleanField(default = False)
#     dateandtime = models.DateTimeField(auto_now_add=True)

    
    # def __str__(self):
    #     return self.subcate_name

    # class Meta:
    #     verbose_name  = "Sub Category"