from django.urls import path

from .api_endpoints import product

app_name = "product"

urlpatterns = [
    path("", product.ProductListView.as_view(), name="product_list"),
    path("<int:product_id>/related-products/", product.RelatedProductListView.as_view(), name="related_products"),
    path("<int:id>/", product.ProductDetailView.as_view(), name="product_detail"),
    # path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
