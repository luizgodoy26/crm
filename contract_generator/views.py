from datetime import date

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from contract_generator.forms import ClientContractForm, ClausuleForm, ItemForm
from contract_generator.models import ClientContract, Item


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



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
    contract_clausules = contract.clausules.all()
    contract_items = contract.items.all()

    total = 0
    for item in contract_items:
        item_total_qt = item.item_qt or 0
        item_total_value = item.item_value or 0
        total += item_total_qt * item_total_value


    context = {'contract': contract,
               'contract_clausules': contract_clausules,
               'contract_items': contract_items,
               'total': total,
    }

    return render(request, 'detail_generated_contract.html', context)




@login_required
def adjust_values(request, id):
    item = get_object_or_404(Item, pk=id)
    # Using instance, the form already start with the data from the client received
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('companies_list')
    return render(request, 'item_form.html', {'form': form, 'item': item})




class ContractToPdf(View):
    def get(self, request, *args, **kwargs):
        template_path = 'generated_contract.html'
        template = get_template(template_path)

        contract = ClientContract.objects.get(pk=self.kwargs['id'])
        contract_items = contract.items.all()

        total = 0
        for item in contract_items:
            item_total_qt = item.item_qt or 0
            item_total_value = item.item_value or 0
            total += item_total_qt * item_total_value

        def get_queryset(self):
            owner = get_object_or_404(ClientContract.objects.filter(user=self.request.user, pk=self.kwargs['id']))
            return owner.user.full_name

        context = {
            'contract': ClientContract.objects.get(pk=self.kwargs['id']),
            'contract_items': ClientContract.objects.get(pk=self.kwargs['id']).items.all(),
            'contract_clausules': ClientContract.objects.get(pk=self.kwargs['id']).clausules.all(),
            'total': total,
            'user': get_queryset(self),
        }
        html = template.render(context)

        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="Contract.pdf"'

        # create a pdf
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response