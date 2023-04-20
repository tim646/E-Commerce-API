from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.cart.models import Cart, CartItem
from apps.product.models import Product


class MiniProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "image",
        )


class CartItemSerializer(ModelSerializer):
    product = MiniProductSerializer()

    class Meta:
        model = CartItem
        fields = (
            "product",
            "quantity",
        )


class MyCartItemSerializer(ModelSerializer):
    items = SerializerMethodField()

    def get_items(self, cart):
        cart_items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(cart_items, many=True)
        return serializer.data

    class Meta:
        model = Cart
        fields = (
            "user",
            "items",
            "total_price",
        )
