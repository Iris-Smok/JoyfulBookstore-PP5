"""context.py for home app"""
# pylint: disable=locally-disabled, no-member
from books.models import Category


def book_categories(request):
    """
    Provides global access to categories
    """
    categories = Category.objects.all().order_by('friendly_name')

    context = {
        'categories': categories,
    }

    return context
