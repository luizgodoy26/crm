from django.shortcuts import render, redirect, get_object_or_404

from contracts.models import Contract
from .models import ClientCompany, ClientPerson, ClientDocuments
from .forms import ClientCompanyForm, ClientPersonForm, FilesForm
from django.contrib.auth.decorators import login_required

from django.db.models import Sum



"""
LIST THE CLIENT COMPANIES
"""
@login_required
def client_company_list(request):
    clients = ClientCompany.objects.filter(user=request.user)
    pending_payments_total = ClientCompany.objects.filter(user=request.user).aggregate(sum=Sum('pending_payments'))['sum'] or 0
    received_payments_total = ClientCompany.objects.filter(user=request.user).aggregate(sum=Sum('received_payments'))['sum'] or 0
    client_count = ClientCompany.objects.filter(user=request.user).count()
    return render(request, 'list_client_company.html', {'clients': clients,
                                                       'pending_payments_total': pending_payments_total,
                                                       'received_payments_total': received_payments_total,
                                                       'client_count': client_count})



"""
LIST THE CLIENT PERSONS
"""
@login_required
def client_person_list(request):
    clients = ClientPerson.objects.filter(user=request.user)
    pending_payments_total = ClientPerson.objects.filter(user=request.user).aggregate(sum=Sum('pending_payments'))['sum'] or 0
    received_payments_total = ClientPerson.objects.filter(user=request.user).aggregate(sum=Sum('received_payments'))['sum'] or 0
    client_count = ClientPerson.objects.filter(user=request.user).count()
    return render(request, 'list_client_person.html', {'clients': clients,
                                                       'pending_payments_total': pending_payments_total,
                                                       'received_payments_total': received_payments_total,
                                                       'client_count': client_count
                                                       })


"""
LIST THE FILES
"""
@login_required
def files_list(request):
    files = ClientDocuments.objects.filter(user=request.user)
    files_count = ClientDocuments.objects.filter(user=request.user).count()
    return render(request, 'list_client_files.html', {'files': files,
                                                       'files_count': files_count})



"""
ADD A NEW CLIENT COMPANY
"""
@login_required
def new_client_company(request):
    # Start post add the company to the DB using POST or start a new form using None
    form = ClientCompanyForm(request.POST, request.FILES, None)

    # Check if the form is valid
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('companies_list')
    return render(request, 'add_client_company_.html', {'form': form})



"""
ADD A NEW CLIENT PERSON
"""
@login_required
def new_client_person(request):
    user = request.user
    form = ClientPersonForm(request.POST or None, request.FILES or None, user=user)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('person_list')
    return render(request, 'add_client_person.html', {'form': form})



"""
ADD A NEW FILE
"""
@login_required
def new_file(request):
    user = request.user
    form = FilesForm(request.POST or None, request.FILES or None, user=user)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('files_list')
    return render(request, 'file_form.html', {'form': form})



#TODO set the client edit to user
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
    return render(request, 'client_company_form.html', {'form': form, 'client': client})



"""
EDIT PERSON CLIENT
"""
@login_required
def edit_client_person(request, id):
    client = get_object_or_404(ClientPerson, pk=id)
    user = request.user
    # Using instance, the form already start with the data from the client received
    form = ClientPersonForm(request.POST or None, request.FILES or None, user=user, instance=client)
    # form = ClientPersonForm(request.POST or None, request.FILES or None, instance=client)


    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'client_person_form.html', {'form': form, 'client': client})



"""
DELETE CLIENT COMPANY
"""
@login_required
def delete_client_company(request, id):
    client = get_object_or_404(ClientCompany, pk=id)

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

    if request.method == 'POST':
        client.delete()
        return redirect('person_list')

    return render(request, 'deletion_client_person_confirm.html', {'client': client})


"""
DELETE FILE
"""
@login_required
def delete_file(request, id):
    file = get_object_or_404(ClientDocuments, pk=id)
    user = request.user

    if request.method == 'POST':
        file.delete()
        return redirect('files_list')

    return render(request, 'deletion_file_confirm.html', {'file': file, 'user':user})




"""
DETAIL CLIENT
"""
@login_required
def detail_client_person(request, id):
    client = get_object_or_404(ClientPerson.objects.filter(user=request.user), pk=id)
    client_files = ClientDocuments.objects.filter(user=request.user, client_person=client)
    contracts = Contract.objects.filter(user=request.user, person_client=client)
    total_received = Contract.objects.filter(user=request.user, person_client=client, status='PD').aggregate(sum=Sum('value'))['sum'] or 0
    total_pending = Contract.objects.filter(user=request.user, person_client=client).aggregate(sum=Sum('value'))['sum'] or 0

    return render(request, 'detail_client_person.html', {'client': client, 'client_files': client_files, 'contracts': contracts, "total_received": total_received, "total_pending": total_pending})



"""
ADD A NEW FILE IN CLIENT DETAIL
"""
@login_required
def new_file_detail(request, id):
    user = request.user
    client = get_object_or_404(ClientPerson, pk=id)
    form = FilesForm(request.POST or None, request.FILES or None, user=user, instance=client, initial={'person_client': client})

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('files_list')
    return render(request, 'file_form.html', {'form': form, 'client': client})
