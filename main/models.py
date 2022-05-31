from email.mime import image
from io import BufferedRandom
from tabnanny import verbose
from turtle import title
from xmlrpc.client import Fault
from django.db import models
from django.utils.html import mark_safe

# Create your models here.
# banner 
class Banner(models.Model):
    img = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=500)
    class Meta:
        verbose_name_plural = "1.Banner"


# brand

class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="brand_img/")
    class Meta:
        verbose_name_plural = "3.Brand"
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "4.Color"
    def __str__(self):
        return self.title

#size 

class Size(models.Model):
    title = models.CharField(max_length=100)
    size_code = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "6.Size"
    def __str__(self):
        return self.title 

# product
class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="prod_img/")
    slug = models.CharField(max_length=100)
    detail = models.TextField()
    price = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "2.Product"
    def __str__(self):
        return self.title 
  

# product attribute
class productAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color,null=True,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,null=True, on_delete=models.CASCADE) 
    price = models.PositiveIntegerField()
    class Meta:
        verbose_name_plural = "5.Products Atribute"
    def __str__(self):
        return self.Product.title