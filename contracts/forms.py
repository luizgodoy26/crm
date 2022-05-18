from django.forms import ModelForm

from clients.models import ClientCompany, ClientPerson
from .models import Contract
from django import forms


"""
FORM FOR CLIENT PERSON
"""
class ContractForm(ModelForm):
    class Meta:
        model = Contract
        widgets = {
            'starting_date': forms.DateInput(format=('%d %b %Y'),attrs={'placeholder':'Date of the contract'},),
            'ending_date': forms.DateInput(format=('%d %b %Y'),attrs={'placeholder':'Ending of the contract'},),
            'payment_date': forms.DateInput(format=('%d %b %Y'),attrs={'placeholder':'Date of payment'},),
        }
        fields = ['contract_name', 'person_client', 'company_client', 'starting_date', 'ending_date', 'payment_date', 'payment_method', 'status', 'value', 'invoice', 'description', 'file']

    def __init__(self,  *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ContractForm, self).__init__(*args, **kwargs)
        self.fields['person_client'].queryset = ClientCompany.objects.filter(user=self.user)
        self.fields['company_client'].queryset = ClientPerson.objects.filter(user=self.user)