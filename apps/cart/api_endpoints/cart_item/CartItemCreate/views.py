from rest_framework.generics import CreateAPIView

from apps.cart.api_endpoints.cart_item.CartItemCreate.serializers import \
    CartItemCreateSerializer
from apps.cart.models import CartItem


class CartItemCreateView(CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateSerializer


__all__ = ['CartItemCreateView']
