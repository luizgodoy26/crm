from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from clients.models import ClientPerson, ClientCompany
from contracts.models import Contract


def dashboard(request):
    return render(request, 'dashboard.html')


# Number of clients
def number_of_clients(request):
    total_clients_p = ClientPerson.objects.filter(user=request.user).count() or 0
    total_clients_c = ClientCompany.objects.filter(user=request.user).count() or 0
    total = total_clients_p+total_clients_c
    if request.method == 'GET':
        return JsonResponse({'total':total})


# Number of contracts
def number_of_contracts(request):
    total = Contract.objects.filter(user=request.user).count() or 0
    if request.method == 'GET':
        return JsonResponse({'total':total})


# Received amount
def total_amount_received(request):
    total = Contract.objects.filter(user=request.user, status='PD').aggregate(sum=Sum('value'))['sum'] or 0
    if request.method == 'GET':
        return JsonResponse({'total':total})


# Pending amount
def total_amount_pending(request):
    total = Contract.objects.filter(user=request.user, status='PN').aggregate(sum=Sum('value'))['sum'] or 0
    if request.method == 'GET':
        return JsonResponse({'total':total})
