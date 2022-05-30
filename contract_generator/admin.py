from django.contrib import admin

# Register your models here.
from contract_generator.models import Item, Clausule, ClientContract

admin.site.register(Item),
admin.site.register(Clausule),
admin.site.register(ClientContract),