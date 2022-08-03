""" shopping_bag context"""
from decimal import Decimal
from django.conf import settings


def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    book_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        "shopping_bag_items": shopping_bag_items,
        "total": total,
        "book_count": book_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,

    }

    return context
