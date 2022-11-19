from django.db import models

# Create your models here.
class blog(models.Model):
    blog_name=models.CharField("Blog Name:",max_length=150)
    blog_title=models.CharField("Blog Title:",max_length=150)
    blog_pics=models.ImageField(upload_to='blogimages/')
    blog_desc=models.TextField("Blog Description:")
    blog_date=models.DateTimeField("Blog Date:",auto_now_add=True)
    isActive=models.BooleanField(default=True)
    
    class Meta:
        verbose_name  = "Blog"
