import django_filters
from django.db.models import Q
from django.forms import TextInput

from .models import Item, ClientContract, Clausule


class ItemFilter(django_filters.FilterSet):
    item = django_filters.CharFilter(method='my_custom_filter', label='Pesquisar', widget=TextInput(attrs={'class': 'search right', 'placeholder': 'Pesquisar item'}))


    class Meta:
        model = Item
        fields = ['item']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(item_name__icontains=value) | Q(unity__icontains=value) | Q(item_type__icontains=value)
        )


class ContractFilter(django_filters.FilterSet):
    contract = django_filters.CharFilter(method='my_custom_filter', label='Pesquisar', widget=TextInput(attrs={'class': 'search right', 'placeholder': 'Pesquisar item'}))


    class Meta:
        model = ClientContract
        fields = ['contract']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(contract_name__icontains=value)
        )



class ClausuleFilter(django_filters.FilterSet):
    clausule = django_filters.CharFilter(method='my_custom_filter', label='Pesquisar', widget=TextInput(attrs={'class': 'search right', 'placeholder': 'Pesquisar item'}))


    class Meta:
        model = Clausule
        fields = ['clausule']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(clausule_name__icontains=value) | Q(clausule_type__icontains=value)
        )