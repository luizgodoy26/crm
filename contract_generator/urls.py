from django.urls import path

from contract_generator.views import new_client_contract, new_clausule, new_item

urlpatterns = [
    path('newct/', new_client_contract, name='new_client_contract'),
    path('newcl/', new_clausule, name='new_clausule'),
    path('newit/', new_item, name='new_item'),

]
