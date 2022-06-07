from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from contract_generator.forms import ClientContractForm, ClausuleForm, ItemForm
from contract_generator.models import ClientContract, Clausule


@login_required
def new_client_contract(request):
    form = ClientContractForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('list_generated_contracts')
    return render(request, 'client_contract_form.html', {'form': form})



@login_required
def new_item(request):
    form = ItemForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('list_generated_contracts')
    return render(request, 'item_form.html', {'form': form})



@login_required
def new_clausule(request):
    form = ClausuleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('list_generated_contracts')
    return render(request, 'clausule_form.html', {'form': form})



@login_required
def list_generated_contracts(request):
    contracts = ClientContract.objects.filter(user=request.user)
    contracts_count = ClientContract.objects.filter(user=request.user).count()
    today = date.today()
    return render(request, 'list_generated_contracts.html', {'contracts': contracts,
                                                  'contracts_count': contracts_count,
                                                  'today':today
                                                  })


@login_required
def edit_generated_contracts(request, id):
    contract = get_object_or_404(ClientContract, pk=id)
    user = request.user

    # Using instance, the form already start with the data from the client received
    form = ClientContractForm(request.POST or None, request.FILES or None, instance=contract)

    if form.is_valid():
        form.save()
        return redirect('list_generated_contracts')
    return render(request, 'client_contract_form.html', {'form': form,
                                                         'contract': contract
                                                         })


"""
DETAIL CONTRACT
"""
@login_required
def detail_generated_contract(request, id):
    contract = get_object_or_404(ClientContract.objects.filter(user=request.user), pk=id)

    return render(request, 'detail_generated_contract.html', {'contract': contract})