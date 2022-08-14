from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def account_overview(request):
    """ Display the account overview"""
    template = 'profiles/account_overview.html'
    context = {}
    return render(request, template, context)


def profile(request):
    """ Display the account overview"""
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)
