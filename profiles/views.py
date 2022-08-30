"""Profile apps vews.py"""
# pylint: disable=locally-disabled, no-member
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


@login_required
def account_overview(request):
    """ Display the account overview"""
    template = 'profiles/account_overview.html'
    return render(request, template)


@login_required
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
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'on_page': True,
    }
    return render(request, template, context)


@login_required
def order_history(request):
    """ Display order history """
    profile = get_object_or_404(UserProfile, user=request.user)
    # get all orders under user name
    orders = profile.orders.all().order_by('-id')
    context = {
        'orders': orders,
        'on_page': True,
    }
    return render(request, 'profiles/order_history.html', context)


@login_required
def order_confirmation(request, order_number):
    """ order confirmation page where user can see order summary"""
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


@login_required
def admin_profile(request):
    """ Display admin account overview"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    template = 'profiles/admin_profile.html'
    return render(request, template)


@login_required
def book_managment(request):
    """ Display book managment page where admin
    can choose to add category and book """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))
    template = 'profiles/book_managment.html'
    return render(request, template)
