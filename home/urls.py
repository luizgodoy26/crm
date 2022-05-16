from django.urls import path
from .views import home #, register_page

urlpatterns = [
    path('', home, name='home'),
    #path('register/', register_page, name='register_page'),
]