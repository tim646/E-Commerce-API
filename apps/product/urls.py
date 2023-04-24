from django.urls import path

from .api_endpoints import product, review, supplier

app_name = "product"

urlpatterns = [
    # product
    path("", product.ProductListView.as_view(), name="product-list"),
    path("<int:product_id>/related-products/", product.RelatedProductListView.as_view(), name="related-products"),
    path("<int:id>/", product.ProductDetailView.as_view(), name="product-detail"),
    path(
        "<int:product_id>/you-may-like-products/",
        product.YouMayLikeProductListView.as_view(),
        name="you-may-like-products",
    ),
    # supplier
    path("supplier/<int:id>/", supplier.SupplierDetailForProductView.as_view(), name="supplier-product-list"),
    path("supplier/<int:id>/detail", supplier.SupplierDetailView.as_view(), name="supplier-detail"),
    #     reviews
    path("review/create/", review.ProductReviewCreateView.as_view(), name="review-create"),
    path("<int:product_id>/review/", review.ProductReviewListView.as_view(), name="review-list"),
    path("<int:product_id>/review/update", review.ProductReviewUpdateView.as_view(), name="review-update"),
]
