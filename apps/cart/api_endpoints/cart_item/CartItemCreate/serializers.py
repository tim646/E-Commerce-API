from rest_framework.serializers import ModelSerializer

from apps.cart.models import CartItem


class CartItemCreateSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            'cart',
            'product',
            'quantity',
        )
