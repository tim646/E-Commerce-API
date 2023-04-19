from django.urls import path

from apps.order.api_endpoints.cart import CartCreateView, CartDeleteView
from apps.order.api_endpoints.cart_item import (CartItemCreateView,
                                                CartItemDeleteView,
                                                CartItemDetailView)
from apps.order.api_endpoints.order import (OrderCreateView, OrderDeleteView,
                                            OrderDetailView, OrderListView)

app_name = "orders"

urlpatterns = [
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order/create/,', OrderCreateView.as_view(), name='order-create'),
    path('order/', OrderListView.as_view(), name="order-list"),
    path('cart/<int:pk>/', CartDeleteView.as_view(), name='cart-delete'),
    path('cart/', CartCreateView.as_view(), name='cart-create'),
    path('cart-item/<int:pk>/delete/', CartItemDeleteView.as_view(), name='cart-item-delete'),
    path('cart-item/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),
    path('cart-item/create/', CartItemCreateView.as_view(), name='cart-item-create'),
]
