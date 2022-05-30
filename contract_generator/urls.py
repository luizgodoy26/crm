from django.urls import path

from contract_generator.views import new_client_contract, new_clausule, new_item, list_generated_contracts, \
    edit_generated_contracts

urlpatterns = [
    path('newct/', new_client_contract, name='new_client_contract'),
    path('newcl/', new_clausule, name='new_clausule'),
    path('newit/', new_item, name='new_item'),

    path('listct/', list_generated_contracts, name='list_generated_contracts'),

    # Edit
    path('editct/<int:id>', edit_generated_contracts, name='edit_generated_contracts'),
]
