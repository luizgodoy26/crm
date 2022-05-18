from django.urls import path
from .views import new_contract

urlpatterns = [
    # List
   path('newct/', new_contract, name='new_contract'),
]