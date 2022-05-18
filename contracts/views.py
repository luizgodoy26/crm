from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ContractForm

"""
ADD A NEW FILE
"""
@login_required
def new_contract(request):
    user = request.user
    form = ContractForm(request.POST or None, request.FILES or None, user=user)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('files_list')
    return render(request, 'contract_form.html', {'form': form})