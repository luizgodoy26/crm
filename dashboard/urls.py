from django.urls import path
#from .views import
from dashboard.views import deashboard

urlpatterns = [
    path('', deashboard, name='dashboard'),
]