from django.forms import ModelForm, DateInput, CheckboxInput

from clients.models import ClientCompany, ClientPerson
from contracts.models import Contract
from .models import Item, Clausule, ClientContract
from django import forms


# Todo: Add delete contracts
# Todo: Fix the bug on contract clausule selection with no cheboxes

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

    fields = ['item_name', 'item_type', 'unity', 'item_qt', 'item_value']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ItemForm, self).__init__(*args, **kwargs)


class ItemFormSimple(ModelForm):
  class Meta:
    model = Item

    fields = ['item_name', 'item_type', 'unity']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ItemForm, self).__init__(*args, **kwargs)



#TODO: adjust the choiche field to display multiple choices fields

class ClientContractForm(ModelForm):
    clausules = forms.CheckboxSelectMultiple()
    work_order = forms.CharField(required=True, label='Ordem de serviço',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    contract_name = forms.CharField(required=True, label='Nome do contrato', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Insira o nome do seu contrato'}))
    address = forms.CharField(required=True, label='Endereço do contrato', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Insira o endereço do contrato'}))
    installments = forms.CharField(required=True, label='Parcelas', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Insira o número de parcelas do contrato'}))
    items = forms.CharField(required=True, label='Itens do contrato', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Insira o número de parcelas do contrato'}))

    class Meta:
        model = ClientContract
        fields = ['work_order', 'contract_name', 'address', 'installments', 'items', 'clausules', 'company_client']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ClientContractForm, self).__init__(*args, **kwargs)
        self.fields['clausules'].queryset = Clausule.objects.filter(user=self.user)
        self.fields['items'].queryset = Item.objects.filter(user=self.user)
        self.fields['work_order'].queryset = Contract.objects.filter(user=self.user)
        self.fields['company_client'].queryset = ClientCompany.objects.filter(user=self.user)
