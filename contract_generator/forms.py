from django.forms import ModelForm, DateInput, CheckboxInput

from clients.models import ClientCompany, ClientPerson
from .models import Item, Clausule, ClientContract
from django import forms


# Todo: Remove the value and quantity from the items on the models
# Todo: Add contracts list
# Todo: Add delete contracts
# Todo: Add edit contracts
# Todo: Fix the bug on contract clausule slection

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
    fields = ['item_name', 'item_type', 'item_value', 'item_quantity', 'unity']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ClausuleForm, self).__init__(*args, **kwargs)



class ClientContractForm(ModelForm):
  class Meta:
    model = ClientContract

    widgets = {
        'starting_date': DateInput(),
        'ending_date': DateInput(),
    }
    fields = ['contract_name', 'person_client', 'company_client', 'phone',
              'email', 'address', 'start_time', 'end_time', 'total_value',
              'installments', 'items', 'clausules']

    # items = forms.ModelMultipleChoiceField(queryset=Item.objects, widget=forms.CheckboxSelectMultiple(),required=False)
    items = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ClausuleForm, self).__init__(*args, **kwargs)
        self.fields['clausules'].queryset = Clausule.objects.filter(user=self.user)
        self.fields['items'].queryset = Item.objects.filter(user=self.user)
        self.fields['company_client'].queryset = ClientCompany.objects.filter(user=self.user)
        self.fields['person_client'].queryset = ClientPerson.objects.filter(user=self.user)