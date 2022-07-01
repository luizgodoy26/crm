import django_filters

from accounts import forms
from . import models
from .models import ClientCompany

class CompanyFilter(django_filters.FilterSet):
    company_name = django_filters.CharFilter(lookup_expr='icontains', label='Search by company name')
    email = django_filters.CharFilter(lookup_expr='icontains', label='Search by email')


    class Meta:
        model = ClientCompany
        fields = ('company_name', 'email')
