from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

import stripe
from shopping_bag.contexts import shopping_bag_contents
from .forms import OrderForm


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(
            request, "There's nothing in your shopping bag at the moment")
        return redirect(reverse('books'))

    current_shopping_bag = shopping_bag_contents(request)
    total = current_shopping_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
