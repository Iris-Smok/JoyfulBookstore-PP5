from django.shortcuts import render


def account_overview(request):
    """ Display the account overview"""
    template = 'profiles/account_overview.html'
    context = {}
    return render(request, template, context)


def profile(request):
    """ Display the account overview"""
    template = 'profiles/profile.html'
    context = {}
    return render(request, template, context)
