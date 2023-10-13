import django_filters
from django.db.models import Q
from django.forms import TextInput

from .models import ClientCompany, ClientPerson


class CompanyFilter(django_filters.FilterSet):
    company = django_filters.CharFilter(method='my_custom_filter', label='Pesquisar', widget=TextInput(attrs={'class': 'search right', 'placeholder': 'Pesquisar cliente'}))


    class Meta:
        model = ClientCompany
        fields = ['company']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(email__icontains=value) | Q(company_name__icontains=value) | Q(company_cnpj__icontains=value)
        )


class PersonFilter(django_filters.FilterSet):
    client = django_filters.CharFilter(method='my_custom_filter', label='Pesquisar', widget=TextInput(attrs={'class': 'search right', 'placeholder': 'Pesquisar cliente'}))


    class Meta:
        model = ClientPerson
        fields = ['client']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value) | Q(cpf__icontains=value) | Q(email__icontains=value)
        )
