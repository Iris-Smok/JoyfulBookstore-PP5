""" newsletter app views"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribers, name='subscribers'),
    path('subscribe_form_post', views.subscribe_form_post, name='subscribers'),
]
