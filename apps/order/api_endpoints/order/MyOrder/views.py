from rest_framework.generics import ListAPIView

from apps.order.api_endpoints.order.MyOrder.serializers import MyOrderListSerializer
from apps.order.models import Order


class MyOrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = MyOrderListSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-created_at")
