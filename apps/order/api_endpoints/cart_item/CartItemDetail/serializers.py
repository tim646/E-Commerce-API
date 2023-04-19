from rest_framework.serializers import ModelSerializer

from apps.order.models import CartItem


class CartItemDetailSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            'cart',
            'product',
            'quantity',
            'created_at',
            'updated_at',
        )
