from django.urls import path

from apps.order.api_endpoints.order import (OrderCreateView, OrderDeleteView,
                                            OrderDetailView, OrderListView)
from apps.order.api_endpoints.order.MyOrder.views import MyOrderListView

app_name = "orders"

urlpatterns = [
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order/create/,', OrderCreateView.as_view(), name='order-create'),
    path('order/', OrderListView.as_view(), name="order-list"),
    path('myorder/', MyOrderListView.as_view(), name="my-order-list"),

]
