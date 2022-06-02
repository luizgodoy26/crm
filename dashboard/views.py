from django.contrib.auth.decorators import login_required
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


def total_month_income(request):
    label = []
    jan = Contract.objects.filter(user=request.user, status='PD', payment_date__month=1).aggregate(sum=Sum('value'))['sum'] or 0
    feb = Contract.objects.filter(user=request.user, status='PD', payment_date__month=2).aggregate(sum=Sum('value'))['sum'] or 0
    mar = Contract.objects.filter(user=request.user, status='PD', payment_date__month=3).aggregate(sum=Sum('value'))['sum'] or 0
    apr = Contract.objects.filter(user=request.user, status='PD', payment_date__month=4).aggregate(sum=Sum('value'))['sum'] or 0
    may = Contract.objects.filter(user=request.user, status='PD', payment_date__month=5).aggregate(sum=Sum('value'))['sum'] or 0
    jun = Contract.objects.filter(user=request.user, status='PD', payment_date__month=6).aggregate(sum=Sum('value'))['sum'] or 0
    jul = Contract.objects.filter(user=request.user, status='PD', payment_date__month=7).aggregate(sum=Sum('value'))['sum'] or 0
    aug = Contract.objects.filter(user=request.user, status='PD', payment_date__month=8).aggregate(sum=Sum('value'))['sum'] or 0
    sep = Contract.objects.filter(user=request.user, status='PD', payment_date__month=9).aggregate(sum=Sum('value'))['sum'] or 0
    oct = Contract.objects.filter(user=request.user, status='PD', payment_date__month=10).aggregate(sum=Sum('value'))['sum'] or 0
    nov = Contract.objects.filter(user=request.user, status='PD', payment_date__month=11).aggregate(sum=Sum('value'))['sum'] or 0
    dec = Contract.objects.filter(user=request.user, status='PD', payment_date__month=12).aggregate(sum=Sum('value'))['sum'] or 0

    data = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
    label = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']


    if request.method == 'GET':
        return JsonResponse({'labels': label, 'data':data})