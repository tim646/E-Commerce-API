from rest_framework.serializers import ModelSerializer, ValidationError

from apps.cart.models import Cart
from apps.order.choices import OrderStatusChoice
from apps.order.models import Order


class OrderCreateSerializer(ModelSerializer):
    def create(self, validated_data):
        user = self.context["request"].user
        try:
            cart = Cart.objects.get(user=user, is_ordered=False)
        except Cart.DoesNotExist:
            raise ValidationError("Cart does not exist or has already been ordered")
        cart.is_ordered = True
        cart.save()
        order = Order.objects.create(
            user=user,
            cart=cart,
            payment_method=validated_data.get("payment_method", OrderStatusChoice.PENDING),
            shipping_cost=validated_data.get("shipping_cost", 0),
            total=cart.total_price,
        )
        return order

    class Meta:
        model = Order
        fields = ("payment_method", "cart", "shipping_cost")
