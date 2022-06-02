from django.urls import path
#from .views import
from dashboard.views import dashboard, number_of_clients, number_of_contracts, total_amount_received, \
    total_amount_pending, total_month_income

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('number_of_clients', number_of_clients, name='number_of_clients'),
    path('number_of_contracts', number_of_contracts, name='number_of_contracts'),
    path('total_amount_received', total_amount_received, name='total_amount_received'),
    path('total_amount_pending', total_amount_pending, name='total_amount_pending'),

    path('total_month_income', total_month_income, name='total_month_income'),
]