from django.urls import path

from apps.order.api_endpoints.order import OrderCreateView, OrderDeleteView, OrderDetailView
from apps.order.api_endpoints.order.MyOrder.views import MyOrderListView

app_name = "orders"

urlpatterns = [
    path("<int:pk>/delete/", OrderDeleteView.as_view(), name="order-delete"),
    path("<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("create/", OrderCreateView.as_view(), name="order-create"),
    path("myorder/", MyOrderListView.as_view(), name="my-order-list"),
]
