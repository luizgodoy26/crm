from django.forms import ModelForm, DateInput, CheckboxInput

from clients.models import ClientCompany, ClientPerson
from contracts.models import Contract
from .models import Item, Clausule, ClientContract
from django import forms



class DateInput(forms.DateInput):
    input_type = 'date'


class ClausuleForm(ModelForm):
    clausule_name = forms.CharField(required=True, label='Nome da cláusula', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Insira o nome da cláusula'}))
    clausule_type = forms.CharField(required=True, label='Tipo de cláusula', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Insira o tipo de cláusula'}))
    clausule_description = forms.CharField(required=False, label='Descrição da cláusula', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Insira a descrição da cláusula'}))

    class Meta:
        model = Clausule
        fields = ['clausule_name', 'clausule_type', 'clausule_description']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ClausuleForm, self).__init__(*args, **kwargs)




class ItemForm(ModelForm):
    item_name = forms.CharField(required=True, label='Nome do item', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Insira o nome do item'}))
    item_qt = forms.CharField(required=True, label='Quantidade', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Insira a quantidade de itens'}))
    item_value = forms.CharField(required=True, label='Valor do item', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Insira o valor dos itens'}))
    item_type = forms.ModelChoiceField(queryset=Item.objects.all(),required=True,label='Tipo de item',widget=forms.Select(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Item
        fields = ['item_name', 'item_type', 'unity', 'item_qt', 'item_value']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['item_type'].label = 'Tipo de item'
        self.fields['unity'].label = 'Unidade de medida'


class ItemFormSimple(ModelForm):
    item_name = forms.CharField(required=True, label='Nome do item', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Insira o nome do item'}))
    item_type = forms.ModelChoiceField(queryset=Item.objects.all(),required=True,label='Tipo de item',widget=forms.Select(
        attrs={'class': 'form-control'}))
    unity = forms.ModelChoiceField(queryset=Item.objects.all(),required=True,label='Unidade de medida',widget=forms.Select(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Item
        fields = ['item_name', 'item_type', 'unity']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ItemFormSimple, self).__init__(*args, **kwargs)
        self.fields['item_type'].label = 'Tipo de item'
        self.fields['unity'].label = 'Unidade de medida'



#TODO: adjust the choiche field to display multiple choices fields

class ClientContractForm(ModelForm):
    work_order = forms.ModelChoiceField(queryset=Contract.objects.all(),required=True,label='Ordem de serviço',widget=forms.Select(
        attrs={'class': 'form-control'}))
    contract_name = forms.CharField(required=True, label='Nome do contrato', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Insira o nome do seu contrato'}))
    address = forms.CharField(required=True, label='Endereço do contrato', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Insira o endereço do contrato'}))
    installments = forms.CharField(required=True, label='Parcelas', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Insira o número de parcelas do contrato'}))
    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), label='Itens do contrato', widget=forms.CheckboxSelectMultiple,
                                               required=False)
    clausules = forms.ModelMultipleChoiceField(queryset=Clausule.objects.all(), label='Cláusulas do contrato', widget=forms.CheckboxSelectMultiple,
                                               required=False)
    company_client = forms.ModelChoiceField(queryset=ClientCompany.objects.all(),required=True,label='Empresa',widget=forms.Select(
        attrs={'class': 'form-control'}))

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
