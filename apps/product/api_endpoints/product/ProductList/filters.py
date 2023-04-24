from django_filters import rest_framework as filters
from apps.product.models import Category, Brand, Feature
from django import forms


class ProductFilter(filters.FilterSet):
    # Add the categories filter
    categories = filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(), widget=forms.SelectMultiple(attrs={"class": "form-control"})
    )
    # Add the brands filter
    brands = filters.ModelMultipleChoiceFilter(
        queryset=Brand.objects.all(), widget=forms.SelectMultiple(attrs={"class": "form-control"})
    )
    # Add the features filter
    features = filters.ModelMultipleChoiceFilter(
        queryset=Feature.objects.all(), widget=forms.SelectMultiple(attrs={"class": "form-control"})
    )
    # Add the price range filter
    price_min = filters.NumberFilter(min_value=0, label="Price Min")
    price_max = filters.NumberFilter(min_value=0, label="Price Max")

    # Define the queryset
    def filter_queryset(self, queryset):
        # Filter by categories
        if self.data.get("categories"):
            categories = self.data.get("categories").split(",")
            queryset = queryset.filter(category__in=categories)

        # Filter by brands
        if self.data.get("brands"):
            queryset = queryset.filter(brand__in=self.data.get("brands"))

        # Filter by features
        if self.data.get("features"):
            queryset = queryset.filter(features__in=self.data.get("features"))

        # Filter by price range
        if self.data.get("price_min") and self.data.get("price_max"):
            queryset = queryset.filter(original_price__range=(self.data.get("price_min"), self.data.get("price_max")))

        return queryset
