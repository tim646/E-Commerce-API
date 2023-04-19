from rest_framework.generics import CreateAPIView

from apps.order.api_endpoints.cart.CartCreate.serializers import \
    CartCreateSerializer
from apps.order.models import Cart


class CartCreateView(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer


__all__ = ['CartCreateView']
