from django.urls import path

from ..wishlist.api_endpoints import wishlist

app_name = "wishlist"

urlpatterns = [
    path("<int:product_id>/wishlist/create/", wishlist.WishlistCreateView.as_view(),
         name="wishlist-create"),
    path("<int:product_id>/wishlist/delete/", wishlist.WishListDeleteView.as_view(),
         name="wishlist-delete"),
    path("", wishlist.WishListAllView.as_view(), name="wishlist-list"),
]
