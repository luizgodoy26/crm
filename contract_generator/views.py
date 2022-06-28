from datetime import date

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from company_profile.models import CompanyProfile
from contract_generator.forms import ClientContractForm, ClausuleForm, ItemForm, ItemFormSimple
from contract_generator.models import ClientContract, Item, Clausule

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa

from contracts.models import Contract
from crmProj.settings import STATIC_ROOT

from crmProj import settings

"""
ADD A NEW CONTRACT
"""
@login_required
def new_client_contract(request):
    form = ClientContractForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('list_generated_contracts')
    return render(request, 'client_contract_form.html', {'form': form})


"""
ADD A NEW ITEM
"""
@login_required
def new_item(request):
    form = ItemFormSimple(request.POST or None, request.FILES or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('list_items')
    return render(request, 'item_form.html', {'form': form})


"""
ADD A NEW CLAUSULE
"""
@login_required
def new_clausule(request):
    form = ClausuleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        return redirect('list_clausules')
    return render(request, 'clausule_form.html', {'form': form})



"""
LIST THE GENERATED CONTRACTS
"""
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


"""
LIST THE ITEMS
"""
@login_required
def list_items(request):
    items = Item.objects.filter(user=request.user)
    items_count = Item.objects.filter(user=request.user).count()
    return render(request, 'list_items.html', {'items': items,
                                                  'items_count': items_count
                                                  })

"""
LIST THE CLAUSULES
"""
@login_required
def list_clausules(request):
    clausules = Clausule.objects.filter(user=request.user)
    clausules_count = Clausule.objects.filter(user=request.user).count()
    return render(request, 'list_clausules.html', {'clausules': clausules,
                                                  'clausules_count': clausules_count
                                                  })

"""
EDIT THE CONTRACT
"""
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
EDIT ITEMS OF THE CONTRACT
"""
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


"""
EDIT CLAUSULES OF THE CONTRACT
"""
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
DETAIL GENERATE CONTRACT
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





"""
ADJUST THE VALUES ON THE GENERATED CONTRACTS
"""
@login_required
def adjust_values(request, id):
    item = get_object_or_404(Item, pk=id)
    # Using instance, the form already start with the data from the client received
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)

    # Get the contract that sent the user to the adjustment page
    if request.method == 'GET':
        request.session['last_contract'] = request.META.get('HTTP_REFERER', '/')

    if form.is_valid():
        form.save()
        # Redirect the user to the contract that sent the user to the adjustment page
        return HttpResponseRedirect(request.session['last_contract'])
    return render(request, 'item_form.html', {'form': form, 'item': item})



"""
DELETE GENERATED CONTRACT
"""
@login_required
def delete_gen_contract(request, id):
    contract = get_object_or_404(ClientContract, pk=id)

    if request.method == 'POST':
        contract.delete()
        return redirect('list_generated_contracts')

    return render(request, 'deletion_gen_contract_confirm.html', {'contract': contract})




"""
DELETE ITEM
"""
@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == 'POST':
        item.delete()
        return redirect('list_items')

    return render(request, 'deletion_item_confirm.html', {'item': item})




"""
DELETE CLAUSULE
"""
@login_required
def delete_clausule(request, id):
    clausule = get_object_or_404(Clausule, pk=id)

    if request.method == 'POST':
        clausule.delete()
        return redirect('clausules_items')

    return render(request, 'deletion_clausule_confirm.html', {'clausule': clausule})



"""
GENERATE CONTRACT PDF
"""
class ContractToPdf(View):
    def get(self, request, *args, **kwargs):
        template_path = 'generated_contract.html'
        template = get_template(template_path)

        contract = ClientContract.objects.get(pk=self.kwargs['id'])
        contract_items = contract.items.all()

        profile = CompanyProfile.objects.filter(user=request.user).first()



        total = 0
        for item in contract_items:
            item_total_qt = item.item_qt or 0
            item_total_value = item.item_value or 0
            total += item_total_qt * item_total_value

        def get_queryset(self):
            owner = get_object_or_404(ClientContract.objects.filter(user=self.request.user, pk=self.kwargs['id']))
            return owner.user.full_name

        counter = 0
        context = {
            'contract': ClientContract.objects.get(pk=self.kwargs['id']),
            'contract_items': ClientContract.objects.get(pk=self.kwargs['id']).items.all(),
            'contract_clausules': ClientContract.objects.get(pk=self.kwargs['id']).clausules.all(),
            'total': total,
            'profile': profile,
            'STATIC_ROOT': STATIC_ROOT,
            'user': get_queryset(self),
            'counter': counter,
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