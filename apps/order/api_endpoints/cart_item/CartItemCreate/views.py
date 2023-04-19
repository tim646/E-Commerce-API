from rest_framework.generics import CreateAPIView

from apps.order.api_endpoints.cart_item.CartItemCreate.serializers import \
    CartItemCreateSerializer
from apps.order.models import CartItem


class CartItemCreateView(CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateSerializer


__all__ = ['CartItemCreateView']
