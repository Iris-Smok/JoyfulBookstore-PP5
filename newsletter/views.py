from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Subscriber, SubscriberEmail
from .forms import EmailForm, SubscriberForm


def newsletter(request):
    """ subscribers page view"""
    all_subscribers = Subscriber.objects.all()
    form = EmailForm()
    template = 'newsletter/newsletter.html'
    context = {

        'form': form,
        'all_subscribers': all_subscribers,

    }
    return render(request, template, context)


def subscribe_form_post(request):
    """ Subscribe form"""

    if request.method == "POST":
        subscribe_form = SubscriberForm(request.POST)
        if subscribe_form.is_valid():
            email = subscribe_form.cleaned_data['email']
            if Subscriber.objects.filter(email=email).exists():
                messages.error(
                    request, f'You are already subscribed with {email}! ')
            else:
                subscribe_form.save()
                messages.success(request, 'Successfully Subscribed.')
        return redirect(reverse("home"))
