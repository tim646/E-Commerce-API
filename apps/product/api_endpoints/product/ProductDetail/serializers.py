from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.product.models import Product, ProductImage


class ProductImagesSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image"]


class ProductDetailSerializer(ModelSerializer):
    category = serializers.StringRelatedField()
    product_type = serializers.StringRelatedField()
    features = serializers.StringRelatedField(many=True)
    images = serializers.SerializerMethodField(read_only=True)
    brand = serializers.StringRelatedField()
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "is_in_stock",
            "color",
            "category",
            "original_price",
            "sell_price",
            "discount_percentage",
            "description",
            "image",
            "product_type",
            "features",
            "brand",
            "material",
            "design",
            "warranty",
            "condition",
            "images",
            "supplier_id",
        ]

    def get_images(self, obj):
        images = obj.images.all()
        serializer = ProductImagesSerializer(images, many=True, context=self.context)
        return serializer.data

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None
