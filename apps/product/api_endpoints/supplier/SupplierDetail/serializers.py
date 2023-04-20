from rest_framework.serializers import ModelSerializer

from apps.product.models import Supplier


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "name", "country", "city", "email", "shipping_type", "image", "is_verified_seller"]


class SupplierDetailForProductSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["name", "country", "city", "shipping_type", "image", "is_verified_seller"]
