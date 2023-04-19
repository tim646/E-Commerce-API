from rest_framework.serializers import ModelSerializer, ValidationError

from apps.cart.models import CartItem


class CartItemUpdateSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            'cart',
            'product',
            'quantity',
        )

    def update(self, instance, validated_data):
        quantity = validated_data.get('quantity')
        if instance.product.quantity < quantity:
            raise ValidationError("Insufficient product quantity")

        if quantity > instance.quantity:
            instance.increment_quantity(quantity - instance.quantity)
        elif quantity < instance.quantity:
            instance.decrement_quantity(instance.quantity - quantity)

        instance.refresh_from_db()

        return instance
