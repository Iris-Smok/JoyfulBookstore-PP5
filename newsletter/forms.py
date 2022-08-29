from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Subscriber, SubscriberEmail


class SubscriberForm(forms.ModelForm):
    """ subscriber form"""
    class Meta:
        model = Subscriber
        fields = ['email', ]
        labels = {
            'email': ''
        }


class EmailForm(forms.ModelForm):
    """ send newsletter form"""
    class Meta:
        model = SubscriberEmail
        fields = ('title', 'message')
        widgets = {
            'message': SummernoteWidget(),
        }
