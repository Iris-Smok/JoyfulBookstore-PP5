""" home page views"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def home_page(request):
    """ home page view"""
    return render(request, 'home/index.html')


def contact_page(request):
    """ contact page view"""

    if request.method == 'POST':
        email_host = settings.DEFAULT_FROM_EMAIL
        try:
            message_email = request.POST['message-email']
            message_name = request.POST['message-name']
            message = request.POST['message']
            messages.success(
                request, f'Thank you {message_name}, your message has been send!')
            send_mail(
                'Message from ' + message_name,  # subject line
                message,  # message
                message_email,  # from email
                [email_host],
            )

            if send_mail:
                send_mail(
                    'Contact confirmation',
                    'Thank you for contacting us! We will get back to you as soon as possbile.',  # message
                    email_host,
                    [message_email],  # from email
                )
            return redirect(reverse('contact'))

        except ValueError:
            messages.error(request, 'Please make sure your form is valid!')

    return render(request, 'home/contact.html')
