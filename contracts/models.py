from django.conf import settings
from django.db import models
from django.urls import reverse

from clients.models import ClientCompany, ClientPerson, ClientDocuments

User = settings.AUTH_USER_MODEL


class Contract(models.Model):

    # Payment options
    IN_CASH = 'IC'
    INSTALLMENTS = 'IS'
    EXCHANGE = 'EX'
    PAYMENT_CHOICES = [
        (IN_CASH, 'In cash'),
        (INSTALLMENTS, 'Installments'),
        (EXCHANGE, 'Exchange'),
    ]

    # Status options
    PAYD = 'PD'
    PENDING = 'PN'
    CANCELLED = 'CC'
    STATUS_CHOICES = (
        (PAYD, "Payd"),
        (PENDING, "Pending"),
        (CANCELLED, "Cancelled"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    contract_name = models.CharField(max_length=90)
    person_client = models.ForeignKey(ClientPerson, null=True, blank=True, on_delete=models.CASCADE)
    company_client = models.ForeignKey(ClientCompany, null=True, blank=True, on_delete=models.CASCADE)

    starting_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    ending_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    payment_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    payment_method = models.CharField(choices=PAYMENT_CHOICES,default=IN_CASH, max_length=20)
    status = models.CharField(choices=STATUS_CHOICES, default=PENDING, max_length=20)

    value = models.DecimalField(max_digits=12, decimal_places=2)

    invoice = models.CharField(blank=True, max_length=90)
    description = models.TextField(blank=True, null=True)
    file = models.ForeignKey(ClientDocuments, null=True, blank=True, on_delete=models.CASCADE)
    # workers = models.ForeignKey(Worker, null=True, blank=True, on_delete=models.PROTECT)

    @property
    def get_html_url(self):
        url = reverse('edit_contract', args=(self.id,))
        return f'<a href="{url}"> {self.contract_name} </a>'

    # To return the name of the person on the django admin
    def __str__(self):
        return self.contract_name