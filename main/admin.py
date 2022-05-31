from turtle import color, title
from django.contrib import admin
from .models import Brand, Color,Product, productAttribute,Banner,Size
# Register your models here.



class Brand_Admin(admin.ModelAdmin):
    list_display = ['id','title','image_tag']
admin.site.register(Brand,Brand_Admin)

class BannerAdmin(admin.ModelAdmin):
    list_display = ['img','alt_text']
   
admin.site.register(Banner,BannerAdmin)    
 
class prod_admin(admin.ModelAdmin):
    list_display = ['id','title','brand','price','status','is_featured']
    list_editable = ['status','is_featured'] 
admin.site.register(Product,prod_admin)

class Color_Admin(admin.ModelAdmin):
    list_display = ['title','color_code']
admin.site.register(Color,Color_Admin)    

class Size_Admin(admin.ModelAdmin):
    list_display = ['id','title','size_code']
admin.site.register(Size,Size_Admin)

class ProdAtribAdmin(admin.ModelAdmin):
    list_display = ['id','product','price']
admin.site.register(productAttribute,ProdAtribAdmin)    
