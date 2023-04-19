from rest_framework.generics import RetrieveAPIView

from apps.order.api_endpoints.cart_item.CartItemDetail.serializers import \
    CartItemDetailSerializer
from apps.order.models import CartItem


class CartItemDetailView(RetrieveAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemDetailSerializer


__all__ = ['CartItemDetailView']
