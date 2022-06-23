from django.urls import path

from contract_generator.views import new_client_contract, new_clausule, new_item, list_generated_contracts, \
    edit_generated_contracts, detail_generated_contract, ContractToPdf, adjust_values, list_items, edit_item

urlpatterns = [
    path('newct/', new_client_contract, name='new_client_contract'),
    path('newcl/', new_clausule, name='new_clausule'),
    path('newit/', new_item, name='new_item'),

    path('', list_generated_contracts, name='list_generated_contracts'),
    path('items/', list_items, name='list_items'),

    path('detailct/<int:id>', detail_generated_contract, name='detail_generated_contract'),

    # Edit
    path('editct/<int:id>', edit_generated_contracts, name='edit_generated_contracts'),
    path('editit/<int:id>', edit_item, name='edit_item'),


    path('adjust_values/<int:id>', adjust_values, name='adjust_values'),


    path('contractpdf/<int:id>', ContractToPdf.as_view(), name='contract_to_pdf'),
]
