from django import forms
from django.forms import ModelForm

from company_profile.models import CompanyProfile

"""
FORM FOR COMPANY PROFILE
"""
class CompanyProfileForm(ModelForm):
    name = forms.CharField(required=True, label='First name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company name'}))
    cnpj = forms.CharField(required=True, label='CNPJ', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company CNPJ'}))
    address = forms.CharField(required=True, label='Address', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company address'}))
    zipcode = forms.IntegerField(required=False, label='Zipcode', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company zipcode'}))

    class Meta:
        model = CompanyProfile
        fields = ['name','cnpj', 'address', 'zipcode', 'logo']

    def __init__(self,  *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CompanyProfileForm, self).__init__(*args, **kwargs)