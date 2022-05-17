from django.forms import ModelForm
from django.http import request
from django.contrib.auth.models import User
from .models import ClientCompany, ClientPerson
from django.contrib.sessions.models import Session

from django import forms
from django.core.validators import RegexValidator

"""
FORM FOR CLIENT COMPANY
"""
class ClientCompanyForm(ModelForm):
    company_name = forms.CharField(required=True, label='Company name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company name'}))
    company_cnpj = forms.IntegerField(required=True, label='CNPJ', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company CNPJ'}))
    phone = forms.IntegerField(required=False, label='Phone', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company phone number'}))
    email = forms.EmailField(required=False, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company e-mail'}))
    pending_payments = forms.DecimalField(required=False, label='Pending payments', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pending payments from the client'}))
    received_payments = forms.DecimalField(required=False, label='Received payments', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Received payments from the client'}))
    class Meta:
        model = ClientCompany
        fields = ['company_name','company_cnpj', 'phone', 'email', 'pending_payments', 'received_payments', 'description']



"""
FORM FOR CLIENT PERSON
"""
class ClientPersonForm(ModelForm):
    first_name = forms.CharField(required=True, label='First name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client first name'}))
    last_name = forms.CharField(required=True, label='Last name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client last name'}))
    cpf = forms.IntegerField(required=True, label='CPF', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client CPF'}))
    phone = forms.IntegerField(required=False, label='Phone', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client phone number'}))
    email = forms.EmailField(required=False, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company e-mail'}))
    pending_payments = forms.DecimalField(required=False, label='Pending payments', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pending payments from the client'}))
    received_payments = forms.DecimalField(required=False, label='Received payments', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Received payments from the client'}))

    class Meta:
        model = ClientPerson
        fields = ['first_name','last_name', 'cpf', 'phone', 'email', 'person_company', 'pending_payments', 'received_payments', 'description']

    def __init__(self,  *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ClientPersonForm, self).__init__(*args, **kwargs)
        self.fields['person_company'].queryset = ClientCompany.objects.filter(user=self.user)