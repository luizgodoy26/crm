from django.forms import ModelForm

from clients.forms import FilesForm
from clients.models import ClientCompany, ClientPerson
from .models import Contract
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

"""
FORM FOR CONTRACT
"""
class ContractForm(ModelForm):
    class Meta:
        model = Contract
        widgets = {
            'starting_date': DateInput(),
            'ending_date': DateInput(),
            'payment_date': DateInput(),
        }
        labels = {
            'contract_name': ('Nome da ordem de serviço'),
            'person_client': ('Pessoa'),
            'company_client': ('Empresa'),
            'starting_date': ('Data de início'),
            'ending_date': ('Data de fim'),
            'payment_date': ('Data de pagamento'),
            'payment_method': ('Meio de pagamento'),
            'status': ('Status'),
            'value': ('Valor'),
            'invoice': ('Nota fiscal'),
            'description': ('Descrição'),
            'file': ('Arquivos')
        }

        fields = ['contract_name', 'person_client', 'company_client', 'starting_date', 'ending_date', 'payment_date', 'payment_method', 'status', 'value', 'invoice', 'description', 'file']

    def __init__(self,  *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ContractForm, self).__init__(*args, **kwargs)
        self.fields['company_client'].queryset = ClientCompany.objects.filter(user=self.user)
        self.fields['person_client'].queryset = ClientPerson.objects.filter(user=self.user)