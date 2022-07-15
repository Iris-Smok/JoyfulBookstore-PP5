""" home page views"""
from django.shortcuts import render


def home_page(request):
    """ home page view"""
    return render(request, 'home/index.html')
