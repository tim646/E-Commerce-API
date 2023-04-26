from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.product.models import Product, ProductImage, Category, ProductType, Feature, Brand, Supplier
from django.core.files.uploadedfile import SimpleUploadedFile

from .serializers import ProductDetailSerializer


class ProductDetailViewTestCase(APITestCase):
    def setUp(self):
        category = Category.objects.create(name="Category 1", thumbnail="Media/category/pic.png")
        feature1 = Feature.objects.create(name="Feature 1", category=category)
        feature2 = Feature.objects.create(name="Feature 2", category=category)
        self.product = Product.objects.create(
            name="Product 1",
            color="Red",
            category=category,
            original_price=100,
            discount_percentage=20,
            description="Description for Product 1",
            product_type=ProductType.objects.create(name="Product Type 1"),
            brand=Brand.objects.create(name="Brand 1"),
            material="Material 1",
            design="Design 1",
            warranty="Warranty 1",
            condition="New",
            supplier=Supplier.objects.create(
                name="Supplier 1",
                country="Country 1",
                city="City 1",
                shipping_type="Shipping Type 1",
                email="supplier1@gmail.com",
            ),
        )
        self.product.features.add(feature1, feature2)
        self.image = ProductImage.objects.create(
            product=self.product, image=SimpleUploadedFile("pic.png", content=b"test image", content_type="image/png")
        )

    def test_retrieve_product_detail(self):
        url = reverse("product:product-detail", args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = ProductDetailSerializer(self.product).data
        self.assertEqual(len(response.data["images"]), len(expected_data["images"]))
        for i, image in enumerate(expected_data["images"]):
            expected_image_url = image["image"]
            expected_image_url = expected_image_url.split("/")[-3:]
            expected_image_url = "/".join(expected_image_url)
            self.assertIn(expected_image_url, response.data["images"][i]["image"])
        expected_data.pop("images")
        response_data = response.data.copy()
        response_data.pop("images")
        self.assertEqual(response_data, expected_data)
