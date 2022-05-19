from django.urls import path
from .views import new_contract, contract_list, edit_contract, delete_contract

urlpatterns = [
    # List
   path('contract/', contract_list, name='contract_list'),

   # Add
   path('newct/', new_contract, name='new_contract'),

   # Edit
   path('editct/<int:id>', edit_contract, name='edit_contract'),

   # Delete
   path('deletect/<int:id>', delete_contract, name='delete_contract'),

]