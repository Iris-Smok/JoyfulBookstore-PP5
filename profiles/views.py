from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def account_overview(request):
    """ Display the account overview"""
    template = 'profiles/account_overview.html'
    return render(request, template)


def profile(request):
    """ Display the account overview"""

    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successfully!')
        else:
            messages.error(
                request,
                "Failed to update profile - please check form and try again")

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'on_profile_page': True,
    }
    return render(request, template, context)


def order_history(request):
    """ Display order history """
    profile = get_object_or_404(UserProfile, user=request.user)
    # get all orders under user name
    orders = profile.orders.all()
    context = {
        'orders': orders,
        'on_profile_page': True,
    }
    return render(request, 'profiles/order_history.html', context)


def order_confirmation(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def admin_profile(request):
    """ Display admin account overview"""
    template = 'profiles/admin_profile.html'
    return render(request, template)


def book_managment(request):
    """ Display book managment page where admin can choose to add category and book """
    template = 'profiles/book_managment.html'
    return render(request, template)
