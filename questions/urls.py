""" FAQ's app views"""

from django.urls import path
from . import views

urlpatterns = [

    path('', views.faq_page, name='faq_page'),
    path('add_faq/', views.add_faq, name='add_faq'),
]
