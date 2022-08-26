from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
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
            email = subscribe_form.cleaned_data['email']
            if Subscriber.objects.filter(email=email).exists():
                messages.error(
                    request, f'You are already subscribed with {email}! ')
            else:
                subscribe_form.save()
                send_mail(
                    'Thank you for subscribing!',
                    'You are subscibed to JoyfulBookstore online newsletter! \n To unsubscribe follow the link https://joyfulbookstore.herokuapp.com/newsletter/unsubscribe',
                    email_host,
                    [email],
                )
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
            body = render_to_string(
                'newsletter/newsletter_emails/newsletter_body.txt', {'message': message})
            send_mail(
                title,
                body,
                '',
                mail_list,
                fail_silently=False,
            )
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
        email = request.POST.get("email")
        try:
            current_subscriber = Subscriber.objects.get(email=email)
            current_subscriber.delete()
            messages.success(
                request,
                f'Successfully unsubscribed email {current_subscriber.email}\
                    from our newsletter')

        except Subscriber.DoesNotExist:
            messages.error(
                request,
                f'The email {email} is not on our list of subscribers')

    return render(request, 'newsletter/unsubscribe.html')
