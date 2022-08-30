""" forms newsletter app"""
from django import forms
from .models import Subscriber, SubscriberEmail


class SubscriberForm(forms.ModelForm):
    """ subscriber form"""
    class Meta:
        """ subscriber form"""
        model = Subscriber
        fields = ['subscriber_email', ]
        labels = {
            'email': ''
        }


class EmailForm(forms.ModelForm):
    """ send newsletter form"""
    class Meta:
        """ newsletter form"""
        model = SubscriberEmail
        fields = ('title', 'message')
