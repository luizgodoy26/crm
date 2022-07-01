import django_filters
from django.forms import TextInput

from accounts import forms
from . import models
from .models import ClientCompany, ClientPerson


class CompanyFilter(django_filters.FilterSet):
    company_name = django_filters.CharFilter(lookup_expr='icontains', label='Search', widget=TextInput(attrs={'class': 'search right', 'placeholder': 'Company name'}))


    class Meta:
        model = ClientCompany
        fields = ['company_name']


class PersonFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains', label='Search by first name')
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Search by last name')


    class Meta:
        model = ClientPerson
        fields = ('first_name', 'last_name')
