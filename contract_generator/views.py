from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from contract_generator.forms import ClientContractForm, ClausuleForm, ItemForm


@login_required
def new_client_contract(request):
    form = ClientContractForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('contract_list')
    return render(request, 'client_contract_form.html', {'form': form})



@login_required
def new_item(request):
    form = ItemForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('contract_list')
    return render(request, 'item_form.html', {'form': form})



@login_required
def new_clausule(request):
    form = ClausuleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('contract_list')
    return render(request, 'clausule_form.html', {'form': form})