import django_filters
from django.db.models import Q
from django.forms import TextInput

from .models import Item


class ItemFilter(django_filters.FilterSet):
    item = django_filters.CharFilter(method='my_custom_filter', label='Search', widget=TextInput(attrs={'class': 'search right', 'placeholder': 'Search item'}))


    class Meta:
        model = Item
        fields = ['item']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(item_name__icontains=value) | Q(unity__icontains=value) | Q(item_type__icontains=value)
        )