from django.contrib import admin
from django.urls import path, include
from clients import urls as clients_urls
from home import urls as home_urls
from accounts import urls as accounts_urls
from contracts import urls as contract_urls
from agenda import urls as agenda_urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home
    path('', include(home_urls)),

    path('register/', include(accounts_urls)),
    path('contracts/', include(contract_urls)),
    path('agenda/', include(agenda_urls)),

    # Login and logout
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),

    # Client application urls
    path('client/', include(clients_urls)),
    path('admin/', admin.site.urls),
]
