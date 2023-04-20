from rest_framework.serializers import ModelSerializer

from apps.product.api_endpoints.product.ProductList.serializers import ProductListSerializer
from apps.wishlist.models import WishList


class WishlistAllSerializer(ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = WishList
        fields = ["product"]
