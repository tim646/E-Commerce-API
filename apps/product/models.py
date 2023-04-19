from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .choices import CONDITION_CHOICES

# Create your models here.


class ProductType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="children")

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="features")

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    country = models.CharField(max_length=50, verbose_name="Country")
    city = models.CharField(max_length=50, verbose_name="City")
    is_verified_seller = models.BooleanField(default=False, verbose_name="Is verified seller")
    shipping_type = models.CharField(max_length=50, verbose_name="Shipping type")
    image = models.ImageField(upload_to="supplier/", blank=True, null=True, verbose_name="Image")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    color = models.CharField(max_length=50, verbose_name="Color")
    features = models.ManyToManyField(Feature, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="products")
    original_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Original price")
    discount_percentage = models.PositiveIntegerField(verbose_name="Discount percentage", default=0)
    quantity = models.IntegerField(verbose_name="Quantity")
    image = models.ImageField(upload_to="product/%Y/%m/%d", blank=True, null=True, verbose_name="Image")
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name="products")
    material = models.CharField(max_length=50, verbose_name="Material")
    warranty = models.CharField(max_length=50, verbose_name="Warranty")
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES, default="New", verbose_name="Condition")

    @property
    def sell_price(self):
        return "{:.2f}".format(self.original_price - (self.original_price * self.discount_percentage / 100))

    @property
    def is_in_stock(self):
        return self.quantity > 0

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product/%Y/%m/%d", verbose_name="Image")

    def __str__(self):
        return self.product.name


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(verbose_name="Rating", validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.TextField(blank=True, null=True, verbose_name="Comment")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")

    def __str__(self):
        return self.product.name
