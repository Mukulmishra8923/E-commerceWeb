from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (Costumer,Product,cart,OrderPlaced,profile_i)


# Register your models here.
@admin.register(Costumer)
class CostumerModelAdmin(admin.ModelAdmin):
    list_display =['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','description','brand','category','product_image']

@admin.register(cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display=['id','user','costumer','product','quantity','ordered_date','status']

# 
admin.site.register(profile_i)