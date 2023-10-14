from django.forms import ModelForm, TextInput
from .models import ClientCompany, ClientPerson, ClientDocuments
from django import forms

"""
FORM FOR CLIENT COMPANY
"""
class ClientCompanyForm(ModelForm):
    company_name = forms.CharField(required=True, label='Empresa', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da empresa'}))
    company_cnpj = forms.CharField(required=True, label='CNPJ', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CNPJ da empresa'}))
    phone = forms.IntegerField(required=False, label='Telefone', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone da empresa'}))
    email = forms.EmailField(required=False, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail da empresa'}))
    pending_payments = forms.DecimalField(required=False, label='Pagamentos pendentes', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pagamentos pendentes da empresa'}))
    received_payments = forms.DecimalField(required=False, label='Pagamentos recebidos', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pagamentos recebidos da empresa'}))
    class Meta:
        model = ClientCompany
        fields = ['company_name','company_cnpj', 'phone', 'email', 'pending_payments', 'received_payments', 'description']



"""
FORM FOR CLIENT PERSON
"""
class ClientPersonForm(ModelForm):
    first_name = forms.CharField(required=True, label='Primeiro nome', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primeiro nome do cliente'}))
    last_name = forms.CharField(required=True, label='Último nome', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Último nome do cliente'}))
    cpf = forms.CharField(required=True, label='CPF', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF do cliente'}))
    phone = forms.IntegerField(required=False, label='Telefone', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone do cliente'}))
    email = forms.EmailField(required=False, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail do cliente'}))
    pending_payments = forms.DecimalField(required=False, label='Pagamentos pendentes', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pagamentos pendentes do cliente'}))
    received_payments = forms.DecimalField(required=False, label='Pagamentos recebidos', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pagamentos recebidos do cliente'}))
    description = forms.CharField(required=False, label='Descrição', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do cliente'}))

    class Meta:
        model = ClientPerson
        fields = ['first_name','last_name', 'cpf', 'phone', 'email', 'person_company', 'pending_payments', 'received_payments', 'description']

    def __init__(self,  *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ClientPersonForm, self).__init__(*args, **kwargs)
        self.fields['person_company'].queryset = ClientCompany.objects.filter(user=self.user)


"""
FORM FOR FILES
"""
class FilesForm(ModelForm):
    name = forms.CharField(required=True, label='Nome do arquivo', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nome do arquivo'}))
    description = forms.CharField(required=True, label='Descrição do arquivo', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Descrição do arquivo'}))
    class Meta:
        model = ClientDocuments
        fields = ['name', 'description', 'client_company', 'client_person', 'file']

    def __init__(self,  *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(FilesForm, self).__init__(*args, **kwargs)
        self.fields['client_company'].queryset = ClientCompany.objects.filter(user=self.user)
        self.fields['client_person'].queryset = ClientPerson.objects.filter(user=self.user)