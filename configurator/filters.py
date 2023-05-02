# filters.py
from django_filters import rest_framework as filters
from .models import *


class ComponentFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = BaseModel
        fields = ['name', 'min_price', 'max_price']
