from django.forms import ModelForm
from .models import ClientCompany, ClientPerson

from django import forms

"""
FORM FOR CLIENT COMPANY
"""
class ClientCompanyForm(ModelForm):
    class Meta:
        model = ClientCompany
        fields = ['company_name','company_cnpj', 'phone', 'email', 'pending_payments', 'received_payments', 'received_payments', 'received_payments', 'description']



"""
FORM FOR CLIENT PERSON
"""
class ClientPersonForm(ModelForm):
    class Meta:
        model = ClientPerson
        fields = ['first_name','last_name', 'cpf', 'phone', 'email', 'person_company', 'pending_payments', 'received_payments', 'description']