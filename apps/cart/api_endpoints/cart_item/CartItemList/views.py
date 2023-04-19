from rest_framework.generics import ListAPIView

from apps.cart.api_endpoints.cart_item.CartItemList.serializers import \
    CartItemListSerializer
from apps.cart.models import CartItem


class CartItemList(ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemListSerializer


__all__ = ['CartItemList']
