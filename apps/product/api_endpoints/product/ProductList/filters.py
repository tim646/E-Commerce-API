import django_filters
from apps.product.models import Product


class ProductFilter(django_filters.FilterSet):
    # Add the categories filter
    categories = django_filters.CharFilter(field_name="category__id", method="filter_categories")

    # Add the brands filter
    brands = django_filters.CharFilter(field_name="brand__id", method="filter_brands")

    # Add the features filter
    features = django_filters.CharFilter(field_name="features__id", method="filter_features")

    # Add the price range filter
    price_min = django_filters.NumberFilter(
        field_name="original_price",
        lookup_expr="gte",
        label="Min price",
    )
    price_max = django_filters.NumberFilter(
        field_name="original_price",
        lookup_expr="lte",
        label="Max price",
    )

    class Meta:
        model = Product
        fields = ["categories", "brands", "features", "price_min", "price_max"]

    def filter_categories(self, queryset, name, value):
        categories = value.split(",")
        return queryset.filter(category__id__in=categories)

    def filter_brands(self, queryset, name, value):
        brands = value.split(",")
        return queryset.filter(brand__id__in=brands)

    def filter_features(self, queryset, name, value):
        features = value.split(",")
        return queryset.filter(features__id__in=features)
