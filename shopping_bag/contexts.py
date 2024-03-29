""" shopping_bag context"""
from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from books.models import Book


def shopping_bag_contents(request):
    """ shopping bag contents"""

    shopping_bag_items = []
    total = 0
    book_count = 0
    shopping_bag = request.session.get('shopping_bag', {})

    for item_id, quantity in shopping_bag.items():
        book = get_object_or_404(Book, pk=item_id)
        total += quantity * book.sort_price
        book_count += quantity
        shopping_bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'book': book,
        })

    if total != 0 and total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY)
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
