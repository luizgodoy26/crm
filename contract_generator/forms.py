from django.forms import ModelForm, DateInput, CheckboxInput

from clients.models import ClientCompany, ClientPerson
from .models import Item, Clausule, ClientContract
from django import forms


# Todo: Add delete contracts
# Todo: Add edit contracts
# Todo: Fix the bug on contract clausule selection

class DateInput(forms.DateInput):
    input_type = 'date'


class ClausuleForm(ModelForm):
  class Meta:
    model = Clausule
    fields = ['clausule_name', 'clausule_type', 'clausule_description']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ClausuleForm, self).__init__(*args, **kwargs)



class ItemForm(ModelForm):
  class Meta:
    model = Item
    fields = ['item_name', 'item_type', 'unity']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ClausuleForm, self).__init__(*args, **kwargs)


class ClientContractForm(ModelForm):
  class Meta:
    model = ClientContract

    widgets = {
        'start_time': DateInput(),
        'end_time': DateInput(),
    }

    fields = ['contract_name', 'person_client', 'company_client', 'phone',
              'email', 'address', 'start_time', 'end_time', 'total_value',
              'installments', 'items', 'clausules']



    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ClausuleForm, self).__init__(*args, **kwargs)
        self.fields['clausules'].queryset = Clausule.objects.filter(user=self.user)
        self.fields['items'].queryset = Item.objects.filter(user=self.user)
        self.fields['company_client'].queryset = ClientCompany.objects.filter(user=self.user)
        self.fields['person_client'].queryset = ClientPerson.objects.filter(user=self.user)