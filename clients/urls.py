from django.urls import path
from .views import client_company_list, client_person_list, new_client_company, new_client_person, edit_client_company, \
    edit_client_person, delete_client_company, delete_client_person, files_list, new_file, delete_file, \
    detail_client_person, new_file_detail, detail_client_company

urlpatterns = [
    # List
    path('companies/', client_company_list, name='companies_list'),
    path('person/', client_person_list, name='person_list'),
    path('files/', files_list, name='files_list'),

    # Detail
    path('detail_client_person/<int:id>', detail_client_person, name='detail_client_person'),
    path('detail_client_company/<int:id>', detail_client_company, name='detail_client_company'),

    # Create
    path('newc/', new_client_company, name='new_client_company'),
    path('newp/', new_client_person, name='new_client_person'),
    path('newf/', new_file, name='new_file'),
    path('newd/<int:id>', new_file_detail, name='new_file_detail'),

    # Edit
    path('editc/<int:id>', edit_client_company, name='edit_client_company'),
    path('editp/<int:id>', edit_client_person, name='edit_client_person'),

    # Delete
    path('deletec/<int:id>', delete_client_company, name='delete_client_company'),
    path('deletep/<int:id>', delete_client_person, name='delete_client_person'),
    path('deletef/<int:id>', delete_file, name='delete_file'),
]