import django_filters
from django.db.models import Q
from django.forms import TextInput

from contracts.models import Contract


class WorkOrderFilter(django_filters.FilterSet):
    work_order = django_filters.CharFilter(method='my_custom_filter', label='Pesquisar', widget=TextInput(attrs={'class': 'search right', 'placeholder': 'Pesquisar item'}))


    class Meta:
        model = Contract
        fields = ['work_order']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(contract_name__icontains=value) | Q(status__icontains=value)
        )