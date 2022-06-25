from datetime import date

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from contract_generator.forms import ClientContractForm, ClausuleForm, ItemForm, ItemFormSimple
from contract_generator.models import ClientContract, Item, Clausule

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



#TODO add list of clausules
from contracts.models import Contract


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
    form = ItemFormSimple(request.POST or None, request.FILES or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('list_items')
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


    # total_value = ClientContract.work_order.objects.filter(user=request.user).aggregate(sum=Sum('value'))['sum'] or 0

    total_value = 0
    for contract in contracts:
        total_value += Contract.objects.filter(user=request.user, clientcontract=contract).aggregate(sum=Sum('value'))['sum'] or 0


    today = date.today()
    return render(request, 'list_generated_contracts.html', {'contracts': contracts,
                                                  'contracts_count': contracts_count,
                                                  'total_value': total_value,
                                                  'today':today
                                                  })


@login_required
def list_items(request):
    items = Item.objects.filter(user=request.user)
    items_count = Item.objects.filter(user=request.user).count()
    return render(request, 'list_items.html', {'items': items,
                                                  'items_count': items_count
                                                  })


@login_required
def list_clausules(request):
    clausules = Clausule.objects.filter(user=request.user)
    clausules_count = Clausule.objects.filter(user=request.user).count()
    return render(request, 'list_clausules.html', {'clausules': clausules,
                                                  'clausules_count': clausules_count
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

@login_required
def edit_item(request, id):
    item = get_object_or_404(Item, pk=id)
    user = request.user

    # Using instance, the form already start with the data from the client received
    form = ItemFormSimple(request.POST or None, request.FILES or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('list_items')
    return render(request, 'item_form.html', {'form': form,
                                                         'item': item
                                                         })

@login_required
def edit_clausule(request, id):
    clausule = get_object_or_404(Clausule, pk=id)
    user = request.user

    # Using instance, the form already start with the data from the client received
    form = ClausuleForm(request.POST or None, request.FILES or None, instance=clausule)

    if form.is_valid():
        form.save()
        return redirect('list_clausules')
    return render(request, 'clausule_form.html', {'form': form,
                                                         'clausule': clausule
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
        return redirect('list_generated_contracts')
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