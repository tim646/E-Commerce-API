from django_filters import rest_framework as filters
from apps.product.models import Product


class ProductFilter(filters.FilterSet):
    # Add the categories filter
    categories = filters.CharFilter(
        field_name="category__name",
        lookup_expr="icontains",
    )

    # Add the brands filter
    brands = filters.CharFilter(
        field_name="brand__name",
        lookup_expr="icontains",
    )

    # Add the features filter
    features = filters.CharFilter(
        field_name="features__name",
        lookup_expr="icontains",
    )

    # Add the price range filter
    price_min = filters.NumberFilter(min_value=0)
    price_max = filters.NumberFilter(min_value=0)

    # Define the queryset
    def filter_queryset(self, queryset):
        data = self.data
        if not data:
            return queryset

        # Filter by categories
        categories = data.getlist("categories")
        if categories:
            queryset = queryset.filter(category__name__in=categories)

        # Filter by brands
        brands = data.getlist("brands")
        if brands:
            queryset = queryset.filter(brand__name__in=brands)

        # Filter by features
        features = data.getlist("features")
        if features:
            queryset = queryset.filter(features__name__in=features)

        # Filter by price range
        price_min = data.get("price_min")
        price_max = data.get("price_max")
        if price_min is not None:
            queryset = queryset.filter(original_price__gte=price_min)
        if price_max is not None:
            queryset = queryset.filter(original_price__lte=price_max)

        return queryset

    class Meta:
        model = Product
        fields = ["categories", "brands", "features", "price_min", "price_max"]
