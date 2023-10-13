from django import forms
from django.forms import ModelForm

from company_profile.models import CompanyProfile

"""
FORM FOR COMPANY PROFILE
"""
class CompanyProfileForm(ModelForm):
    name = forms.CharField(required=True, label='Nome', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da empresa'}))
    cnpj = forms.CharField(required=True, label='CNPJ', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CNPJ da empresa'}))
    address = forms.CharField(required=True, label='Endereço', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço da empresa'}))
    zipcode = forms.IntegerField(required=False, label='CEP', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP da empresa'}))

    class Meta:
        model = CompanyProfile
        fields = ['name','cnpj', 'address', 'zipcode', 'logo']

    def __init__(self,  *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CompanyProfileForm, self).__init__(*args, **kwargs)