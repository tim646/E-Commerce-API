from django.contrib import admin
from .models import Category, Brand, ProductType, Supplier, Feature, Product,  ProductImage, ProductReview
# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductType)
admin.site.register(Supplier)
admin.site.register(Feature)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
