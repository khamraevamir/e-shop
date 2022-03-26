from unicodedata import category
from django.contrib import admin
from .models import Brand, Cart,Order, Category, Color, Memory, OrderProduct, Product, ProductColor, ProductColorSize, ProductGallery



class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "brand", "category")
    
class ProductColorSizeAdmin(admin.ModelAdmin):
    list_display = ("productColor", "memory", "price")


class ProductColorAdmin(admin.ModelAdmin):
    list_display = ("product", "color")

class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "product", 'quantity')


admin.site.register(Cart, CartAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductColorSize, ProductColorSizeAdmin)
admin.site.register(ProductColor, ProductColorAdmin)


admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Brand)

admin.site.register(Memory)
admin.site.register(ProductGallery)

admin.site.register(Order)
admin.site.register(OrderProduct)