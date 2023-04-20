from rest_framework.generics import ListAPIView

from apps.cart.api_endpoints.cart.MyCartItems.filters import IsOwnerFilterBackend
from apps.cart.api_endpoints.cart.MyCartItems.serializers import MyCartItemSerializer
from apps.cart.models import Cart
from apps.common.permissions import IsOwnerOrReadOnly


class MyCartItemView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = MyCartItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [IsOwnerFilterBackend]


__all__ = ["MyCartItemView"]
