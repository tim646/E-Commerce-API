from django.urls import path

from apps.cart.api_endpoints.cart import CartCreateView, CartDeleteView, MyCartItemView
from apps.cart.api_endpoints.cart_item import (
    CartItemCreateView,
    CartItemDeleteView,
    CartItemDetailView,
    CartItemUpdateView,
)

app_name = "cart"

urlpatterns = [
    path("<int:pk>/", CartDeleteView.as_view(), name="cart-delete"),
    path("", CartCreateView.as_view(), name="cart-create"),
    path("mycart/", MyCartItemView.as_view(), name="my-cart"),
    path("item/<int:pk>/delete/", CartItemDeleteView.as_view(), name="cart-item-delete"),
    path("item/<int:pk>/update/", CartItemUpdateView.as_view(), name="cart-item-delete"),
    path("item/<int:pk>/", CartItemDetailView.as_view(), name="cart-item-detail"),
    path("item/create/", CartItemCreateView.as_view(), name="cart-item-create"),
]
