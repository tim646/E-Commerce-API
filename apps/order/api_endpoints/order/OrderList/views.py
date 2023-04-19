from rest_framework.generics import ListAPIView

from apps.order.api_endpoints.order.OrderList.serializers import \
    OrderListSerializer
from apps.order.models import Order


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


__all__ = ["OrderListView"]
