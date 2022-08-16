from books.models import Category


def book_categories(request):
    """
    Provides global access to categories
    """
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return context
