from django.urls import path

from contract_generator.views import new_client_contract, new_clausule, new_item, list_generated_contracts, \
    edit_generated_contracts, detail_generated_contract, ContractToPdf, adjust_values, list_items, edit_item, \
    list_clausules, edit_clausule, delete_gen_contract, delete_item, delete_clausule


urlpatterns = [
    # Create
    path('newct/', new_client_contract, name='new_client_contract'),
    path('newcl/', new_clausule, name='new_clausule'),
    path('newit/', new_item, name='new_item'),


    # List
    path('', list_generated_contracts, name='list_generated_contracts'),
    path('items/', list_items, name='list_items'),
    path('clausules/', list_clausules, name='list_clausules'),


    # Detail
    path('detailct/<int:id>', detail_generated_contract, name='detail_generated_contract'),


    # Edit
    path('editct/<int:id>', edit_generated_contracts, name='edit_generated_contracts'),
    path('editit/<int:id>', edit_item, name='edit_item'),
    path('editcl/<int:id>', edit_clausule, name='edit_clausule'),
    path('adjust_values/<int:id>', adjust_values, name='adjust_values'),


    # Delete
    path('deletect/<int:id>', delete_gen_contract, name='delete_gen_contract'),
    path('deleteit/<int:id>', delete_item, name='delete_item'),
    path('deletecl/<int:id>', delete_clausule, name='delete_clausule'),

    # Generate contract PDF
    path('contractpdf/<int:id>', ContractToPdf.as_view(), name='contract_to_pdf'),
]
