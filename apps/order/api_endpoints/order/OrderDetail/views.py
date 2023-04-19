from rest_framework.generics import RetrieveAPIView

from apps.order.api_endpoints.order.OrderDetail.serializers import \
    OrderDetailSerializer
from apps.order.models import Order


class OrderDetailView(RetrieveAPIView):
    queryset = Order
    serializer_class = OrderDetailSerializer


__all__ = ["OrderDetailView"]
