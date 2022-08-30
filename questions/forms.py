""" faq forms.py"""
from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    """ FAQ's form """
    class Meta:
        """ faq form"""
        model = Question
        fields = '__all__'
