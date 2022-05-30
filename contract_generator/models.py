from django.conf import settings
from django.db import models

from clients.models import ClientPerson, ClientCompany

User = settings.AUTH_USER_MODEL


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    item_name = models.CharField(max_length=90)
    item_type = models.CharField(max_length=90)

    # Unity options
    METERS = 'MT'
    LITERS = 'LT'
    UNITY_CHOICES = [
        (METERS, 'Meters'),
        (LITERS, 'Liters'),
    ]

    unity = models.CharField(choices=UNITY_CHOICES, default=METERS, max_length=20)

    def __str__(self):
        return self.item_name


class Clausule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    clausule_name = models.CharField(max_length=60)
    clausule_type = models.CharField(max_length=60)

    clausule_description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.clausule_name

class ClientContract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    contract_name = models.CharField(max_length=60)

    # Client related information
    person_client = models.ForeignKey(ClientPerson, null=True, blank=True, on_delete=models.PROTECT)
    company_client = models.ForeignKey(ClientCompany, null=True, blank=True, on_delete=models.PROTECT)

    # Contact related information
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)

    # Date related information
    start_time = models.DateField(null=True, blank=True)
    end_time = models.DateField(null=True, blank=True)


    # Value related information
    total_value = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    installments = models.IntegerField(null=True, blank=True)


    # Items and clausules of the contract
    items = models.ManyToManyField(Item, blank=True, null=True)
    clausules = models.ManyToManyField(Clausule, blank=True, null=True)


    def __str__(self):
        return self.contract_name