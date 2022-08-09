from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(
            request, "There's nothing in your shopping bag at the moment")
        return redirect(reverse('books'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LUoQrApowAGG2zDZ2VqhMjRJgNLuT4zAYz9JKImlSXPUhGvHMoFLqUAvbbYG3ihDDDcadoc06QofTNHtqWZxagQ00a8b5Ogwy',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
