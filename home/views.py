from django.shortcuts import render
from django.contrib.auth import get_user_model

from .forms import RegisterForm

"""
HOME PAGE
"""


def home(request):
    return render(request, 'home.html')


# User = get_user_model()
# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context = {
#         'form': form
#     }
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         email = form.cleaned_data.get('email')
#         password = form.cleaned_data.get('password')
#         new_user = User.objects.create_user(username, email, password)
#     return render(request, 'registration/register.html', context)

