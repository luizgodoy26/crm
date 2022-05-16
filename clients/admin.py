from django.contrib import admin
from .models import ClientPerson, ClientCompany, ClientDocuments

admin.site.register(ClientPerson)
admin.site.register(ClientCompany)
admin.site.register(ClientDocuments)
