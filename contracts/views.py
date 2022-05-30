from datetime import datetime, date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from clients.forms import FilesForm
from .forms import ContractForm
from .models import Contract

from django.db.models import Sum

"""
ADD A NEW CONTRACT
"""
@login_required
def new_contract(request):
    user = request.user
    form = ContractForm(request.POST or None, request.FILES or None, user=user)
    files_form = FilesForm(request.POST or None, request.FILES or None, user=user)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('contract_list')
    return render(request, 'contract_form.html', {'form': form})


"""
LIST CONTRACT
"""
@login_required
def contract_list(request):
    contracts = Contract.objects.filter(user=request.user)
    total_contracts_value = Contract.objects.filter(user=request.user).aggregate(sum=Sum('value'))['sum'] or 0
    contracts_count = Contract.objects.filter(user=request.user).count()
    today = date.today()
    return render(request, 'list_contract.html', {'contracts': contracts,
                                                       'total_contracts_value': total_contracts_value,
                                                       'contracts_count': contracts_count, 'today':today})


"""
EDIT COMPANY CLIENT
"""
@login_required
def edit_contract(request, id):
    contract = get_object_or_404(Contract, pk=id)
    user = request.user

    # Using instance, the form already start with the data from the client received
    form = ContractForm(request.POST or None, request.FILES or None, user=user, instance=contract)

    if form.is_valid():
        form.save()
        return redirect('contract_list')
    return render(request, 'contract_form.html', {'form': form, 'contract': contract})


"""
DELETE CLIENT PERSON
"""
@login_required
def delete_contract(request, id):
    contract = get_object_or_404(Contract, pk=id)

    if request.method == 'POST':
        contract.delete()
        return redirect('contract_list')

    return render(request, 'deletion_contract_confirm.html', {'contract': contract})
