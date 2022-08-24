from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
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


def newsletter_email(request):
    """ A view to allow superusers to send an email to their subscriber list """
    emails = Subscriber.objects.all()
    dataframe = read_frame(emails, fieldnames=['email'])
    mail_list = dataframe['email'].values.tolist()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid:
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request,
                             'You Have Sent Your Newsletter \
                              To Your Subscribers.')
            return redirect(reverse("newsletter"))
            print(form)
            print(mail_list)
    else:
        form = EmailForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/newsletter.html', context)
