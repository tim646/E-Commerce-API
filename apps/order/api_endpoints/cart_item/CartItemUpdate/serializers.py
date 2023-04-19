from rest_framework.serializers import ModelSerializer

from apps.order.models import CartItem


class CartItemUpdateSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            'cart',
            'product',
            'quantity',
        )
