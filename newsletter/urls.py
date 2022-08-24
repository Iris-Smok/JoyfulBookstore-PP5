""" newsletter app views"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('subscribe_form_post', views.subscribe_form_post, name='subscribers'),
]
