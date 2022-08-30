"""shopping_bag template tags"""
from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ calc subtotal function"""
    return price * quantity
