from django.shortcuts import render, redirect, get_object_or_404
from .models import ClientCompany, ClientPerson
from .forms import ClientCompanyForm, ClientPersonForm
from django.contrib.auth.decorators import login_required

from django.db.models import Sum

"""
LIST THE CLIENT COMPANIES
"""
@login_required
def client_company_list(request):
    clients = ClientCompany.objects.all()
    pending_payments_total = ClientCompany.objects.aggregate(sum=Sum('pending_payments'))['sum'] or 0
    received_payments_total = ClientCompany.objects.aggregate(sum=Sum('received_payments'))['sum'] or 0
    client_count = ClientCompany.objects.filter().count()
    return render(request, 'list_client_company.html', {'clients': clients,
                                                       'pending_payments_total': pending_payments_total,
                                                       'received_payments_total': received_payments_total,
                                                       'client_count': client_count})



"""
LIST THE CLIENT PERSONS
"""
@login_required
def client_person_list(request):
    clients = ClientPerson.objects.all()
    pending_payments_total = ClientPerson.objects.aggregate(sum=Sum('pending_payments'))['sum'] or 0
    received_payments_total = ClientPerson.objects.aggregate(sum=Sum('received_payments'))['sum'] or 0
    client_count = ClientPerson.objects.filter().count()
    return render(request, 'list_client_person.html', {'clients': clients,
                                                       'pending_payments_total': pending_payments_total,
                                                       'received_payments_total': received_payments_total,
                                                       'client_count': client_count
                                                       })



"""
ADD A NEW CLIENT COMPANY
"""
@login_required
def new_client_company(request):
    # Start post add the company to the DB using POST or start a new form using None
    form = ClientCompanyForm(request.POST, request.FILES, None)

    # Check if the form is valid
    if form.is_valid():
        form.save()
        return redirect('companies_list')
    return render(request, 'client_company_form.html', {'form': form})



"""
ADD A NEW CLIENT PERSON
"""
@login_required
def new_client_person(request):
    form = ClientPersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'client_person_form.html', {'form': form})



"""
EDIT COMPANY CLIENT
"""
@login_required
def edit_client_company(request, id):
    client = get_object_or_404(ClientCompany, pk=id)
    # Using instance, the form already start with the data from the client received
    form = ClientCompanyForm(request.POST or None, request.FILES or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('companies_list')
    return render(request, 'client_company_form.html', {'form': form})



"""
EDIT PERSON CLIENT
"""
@login_required
def edit_client_person(request, id):
    client = get_object_or_404(ClientPerson, pk=id)
    # Using instance, the form already start with the data from the client received
    form = ClientPersonForm(request.POST or None, request.FILES or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'client_person_form.html', {'form': form})



"""
DELETE CLIENT COMPANY
"""
@login_required
def delete_client_company(request, id):
    client = get_object_or_404(ClientCompany, pk=id)
    form = ClientCompanyForm(request.POST or None, request.FILES or None, instance=client)

    if request.method == 'POST':
        client.delete()
        return redirect('companies_list')

    return render(request, 'deletion_client_company_confirm.html', {'client': client})



"""
DELETE CLIENT PERSON
"""
@login_required
def delete_client_person(request, id):
    client = get_object_or_404(ClientPerson, pk=id)
    form = ClientPersonForm(request.POST or None, request.FILES or None, instance=client)

    if request.method == 'POST':
        client.delete()
        return redirect('person_list')

    return render(request, 'deletion_client_person_confirm.html', {'client': client})