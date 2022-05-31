from operator import index
from django.shortcuts import render
from . models import Brand, Product, productAttribute

# Create your views here.
# home page
def IndexPage(request):
    return render(request,'index.html')

def BrandFun(request):
    data=Brand.objects.all()
    return render(request,'brands.html',{'data':data})






def ProductFun(request):
    data=Product.objects.all().order_by('-id')
    brand = Product.objects.distinct().values('brand__title','brand__id')
    color = productAttribute.objects.distinct().values('color__title','color__id','color__color_code')
    size = productAttribute.objects.distinct().values('size__title','size__id')
    return render(request,'product.html',{'data':data,'brand':brand,'size':size,'color':color})
                    
                      