from django.conf import settings
from django.db import models

from clients.models import ClientPerson, ClientCompany
from contracts.models import Contract

User = settings.AUTH_USER_MODEL


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    item_name = models.CharField(max_length=90)
    item_type = models.CharField(max_length=90)

    item_value = models.FloatField(blank=True, null=True, max_length=12)
    item_qt = models.FloatField(blank=True, null=True, max_length=12)
    item_total = models.FloatField(blank=True, null=True, max_length=12)

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
    original_contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, blank=True)
    contract_name = models.CharField(max_length=60)
    address = models.TextField(blank=True, null=True)

    # Value related information
    total_value = models.DecimalField(blank=True, null=True, max_digits=12, decimal_places=2)
    installments = models.IntegerField(null=True, blank=True)

    # Items and clausules of the contract
    items = models.ManyToManyField(Item, blank=True, null=True)
    clausules = models.ManyToManyField(Clausule, blank=True, null=True)


    def __str__(self):
        return self.contract_name