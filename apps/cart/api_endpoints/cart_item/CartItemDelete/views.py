from rest_framework.generics import DestroyAPIView

from apps.cart.api_endpoints.cart_item.CartItemDelete.serializers import \
    CartItemDeleteSerializer
from apps.cart.models import CartItem


class CartItemDeleteView(DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemDeleteSerializer


__all__ = ['CartItemDeleteView']
