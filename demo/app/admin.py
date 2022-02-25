from unicodedata import category
from django.contrib import admin
from .models import Brand, Cart, Category, Color, Memory, Product, ProductColor, ProductColorSize, ProductGallery

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductColor)
admin.site.register(Memory)
admin.site.register(ProductGallery)
admin.site.register(ProductColorSize)
admin.site.register(Cart)