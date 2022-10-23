from datetime import datetime, date

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


#TODO get the top 5 contracts income
def total_client_income(request):
    label = []
    today = date.today()
    month = Contract.objects.filter(user=request.user, status='PD', starting_date__year=today.year, starting_date__month=today.month)#.aggregate(sum=Sum('value'))['sum'] or 0

    for client in month:
        client.received_payments = Contract.objects.filter(user=request.user, company_client=client, status='PD').aggregate(sum=Sum('value'))['sum'] or 0
        client.pending_payments = Contract.objects.filter(user=request.user, company_client=client, status='PN').aggregate(sum=Sum('value'))['sum'] or 0


    teste = month.oder_by('received_payments').head(5)
    print(month)

    data = [month]
    label = ['month']


    if request.method == 'GET':
        return JsonResponse({'labels': label, 'data':data})


def top_five_client_income (request):
    today = date.today()
    clients_c = ClientCompany.objects.filter(user=request.user)
    clients_p = ClientPerson.objects.filter(user=request.user)

    values_by_client = []
    client_names = []
    data = []
    label = []

    for client in clients_c:
        client_value_c = float(Contract.objects.filter(user=request.user, company_client=client, status='PD', starting_date__year=today.year).aggregate(sum=Sum('value'))['sum'] or 0)
        client_data = {'name':client.company_name,'value':client_value_c}
        values_by_client.append(client_data)
        client_names.append(client_data)

    for client in clients_p:
        client_value_p = float(Contract.objects.filter(user=request.user, person_client=client, status='PD', starting_date__year=today.year).aggregate(sum=Sum('value'))['sum'] or 0)
        client_data = {'name':client.first_name,'value':client_value_p}
        values_by_client.append(client_data)
        client_names.append(client_data)




    # # Get the 5 highest values on the list
    values_by_client = sorted(values_by_client, key=lambda x: x['value'], reverse=True)[:5]
    print(values_by_client)

    # Input contract values on data[]
    for value in values_by_client:
        data.append(value.get('value'))
    # Input contract name  on label[]
    for client in values_by_client:
        label.append(client.get('name'))

    print(label)

    if request.method == 'GET':
        return JsonResponse({'labels': label, 'data':data})