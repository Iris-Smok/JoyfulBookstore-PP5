from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mass_mail
from django.core.mail import send_mail
from django_pandas.io import read_frame
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.template.loader import render_to_string
from .models import Subscriber, SubscriberEmail
from .forms import EmailForm, SubscriberForm


def newsletter(request):
    """ subscribers page view"""
    all_subscribers = Subscriber.objects.all()
    form = EmailForm()
    template = 'newsletter/newsletter_admin.html'
    context = {

        'form': form,
        'all_subscribers': all_subscribers,
        'on_page': True,

    }
    return render(request, template, context)


def subscribe_form_post(request):
    """ Subscribe form"""

    if request.method == "POST":
        subscribe_form = SubscriberForm(request.POST)
        email_host = settings.DEFAULT_FROM_EMAIL
        if subscribe_form.is_valid():
            subscriber_email = subscribe_form.cleaned_data['subscriber_email']
            if Subscriber.objects.filter(subscriber_email=subscriber_email).exists():
                messages.error(
                    request, f'You are already subscribed with {subscriber_email}! ')
            else:
                subscribe_form.save()
                send_mail(
                    'Thank you for subscribing!',
                    'You are subscibed to JoyfulBookstore online newsletter! \n To unsubscribe follow the link https://joyfulbookstore.herokuapp.com/newsletter/unsubscribe',
                    email_host,
                    [subscriber_email],
                )
                messages.success(request, 'Successfully Subscribed.')

        context = {
            'on_page': True,

        }
        return redirect(reverse("home"), context)


def newsletter_email(request):
    """ A view to allow superusers to send an email to their subscriber list """
    emails = Subscriber.objects.all()
    email_host = settings.DEFAULT_FROM_EMAIL
    dataframe = read_frame(emails, fieldnames=['subscriber_email'])
    mail_list = dataframe['subscriber_email'].values.tolist()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid:
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            body = render_to_string(
                'newsletter/newsletter_emails/newsletter_body.txt', {'message': message})
            email = [(title, body, email_host, [recipient])
                     for recipient in mail_list]
            send_mass_mail(email)
            messages.success(request,
                             'You Have Sent Your Newsletter \
                              To Your Subscribers.')

            return redirect(reverse("newsletter"))
    else:
        form = EmailForm()
        messages.error(request, 'Please check the form and try again')
        return redirect(reverse("newsletter"))

    context = {
        'form': form,
        'on_page': True
    }
    return render(request, 'newsletter/newsletter.html', context)


def unsubscribe(request):
    """ unsubscribe from newsletter"""
    if request.method == 'POST':
        subscriber_email = request.POST.get("email-unsubscribe")
        try:
            current_subscriber = Subscriber.objects.get(
                subscriber_email=subscriber_email)
            current_subscriber.delete()
            messages.success(
                request,
                f'Successfully unsubscribed email {current_subscriber.subscriber_email}\
                    from our newsletter')

        except Subscriber.DoesNotExist:
            messages.error(
                request,
                f'The email {subscriber_email} is not on our list of subscribers')
    context = {
        'on_page': True,

    }

    return render(request, 'newsletter/unsubscribe.html', context)
