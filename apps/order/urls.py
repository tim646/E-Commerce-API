from django.urls import path

from apps.order.api_endpoints.order import OrderCreateView

app_name = "orders"

urlpatterns = [
    path("OrderCrete/", OrderCreateView.as_view(), name="order-create"),
]
