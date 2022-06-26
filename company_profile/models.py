from django.conf import settings
from django.db import models
from django_cpf_cnpj.fields import CNPJField

User = settings.AUTH_USER_MODEL

# Company client
class CompanyProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=60)
    cnpj = CNPJField(masked=True)
    address = models.CharField(null=True, blank=True, max_length=250)
    zipcode = models.IntegerField(null=True, blank=True)
    logo = models.ImageField(upload_to='user_files')

    # To return the name of the company on the django admin
    def __str__(self):
        return self.name