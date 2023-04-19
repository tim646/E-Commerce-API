from rest_framework.generics import RetrieveAPIView

from apps.cart.api_endpoints.cart_item.CartItemDetail.serializers import \
    CartItemDetailSerializer
from apps.cart.models import CartItem


class CartItemDetailView(RetrieveAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemDetailSerializer


__all__ = ['CartItemDetailView']
