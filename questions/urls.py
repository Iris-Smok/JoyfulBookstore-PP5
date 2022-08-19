""" FAQ's app views"""

from django.urls import path
from . import views

urlpatterns = [

    path('', views.faq_page, name='faq_page'),

]
