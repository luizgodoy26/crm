from django.conf import settings
from django.db import models
from django_cpf_cnpj.fields import CNPJField, CPFField

User = settings.AUTH_USER_MODEL

# Company client
class ClientCompany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    company_name = models.CharField(max_length=30)
    company_cnpj = CNPJField(masked=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    # To return the name of the company on the django admin
    def __str__(self):
        return self.company_name


# Person Client
class ClientPerson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=90)
    cpf = CPFField(masked=False)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    person_company = models.ForeignKey(ClientCompany, null=True, blank=True, on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)

    # To return the name of the person on the django admin
    def __str__(self):
        return self.first_name


# Documents
class ClientDocuments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    file = models.FileField(upload_to='clients_files')

    client_company = models.ForeignKey(ClientCompany, null=True, blank=True, on_delete=models.PROTECT)
    client_person = models.ForeignKey(ClientPerson, null=True, blank=True, on_delete=models.PROTECT)

    # To return the name of the person on the django admin
    def __str__(self):
        return self.name