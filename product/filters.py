from django_filters.rest_framework import FilterSet  # type: ignore
from product.models import Product

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category_id':['exact'],
            'price': ['gt', 'lt']
        }