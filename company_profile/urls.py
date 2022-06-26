from django.urls import path
from .views import edit_company_profile, detail_company_profile, add_company_profile

urlpatterns = [
    # Edit
    path('editcp/<int:id>', edit_company_profile, name='edit_company_profile'),

    # Add
    path('add/', add_company_profile, name='add_company_profile'),

    # Detail
    path('detailcp/<int:id>', detail_company_profile, name='detail_company_profile'),
]