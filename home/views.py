from django.shortcuts import render, redirect

"""
HOME PAGE
"""
def home(request):
    return render(request, 'home.html')
