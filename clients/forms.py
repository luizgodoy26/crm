from django.forms import ModelForm
from .models import ClientCompany, ClientPerson

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
    class Meta:
        model = ClientPerson
        fields = ['first_name','last_name', 'cpf', 'phone', 'email', 'person_company', 'pending_payments', 'received_payments', 'description']