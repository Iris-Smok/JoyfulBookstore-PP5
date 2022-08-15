from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def account_overview(request):
    """ Display the account overview"""
    template = 'profiles/account_overview.html'
    context = {}
    return render(request, template, context)


def profile(request):
    """ Display the account overview"""

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, template, context)


def order_history(request):
    """ Display order history """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.objects.all()
    template = 'profiles/order_history'
    context = {}
    return render(request, template, context)
