from django.contrib import admin

from .models import Brand, Category, Feature, Product, ProductImage, ProductReview, ProductType, Supplier

# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductType)
admin.site.register(Supplier)
admin.site.register(Feature)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
