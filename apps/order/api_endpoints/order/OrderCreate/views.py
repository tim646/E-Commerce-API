from rest_framework.generics import CreateAPIView

from apps.order.api_endpoints.order.OrderCreate.serializers import OrderCreateSerializer
from apps.order.models import Order


class OrderCreateView(CreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()


__all__ = ["OrderCreateView"]
