""" shopping_bag viewspy"""
from django.shortcuts import (
    render, redirect, reverse,
    get_object_or_404, HttpResponse)
from django.contrib import messages
from books.models import Book


def shopping_bag_view(request):
    """ A view that render the shopping_bag content"""
    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ Add a quantity of the book to the shopping bag"""

    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
        shopping_bag[item_id] = quantity
    messages.success(request, f'Added {book.title} to your shopping bag')

    request.session['shopping_bag'] = shopping_bag
    return(redirect(redirect_url))


def adjust_shopping_bag(request, item_id):
    """ Ajust quantity of the book to the specified amount"""

    book = get_object_or_404(Book, pk=item_id)
    quantity = int(request.POST.get('quantity') or 1)
    shopping_bag = request.session.get('shopping_bag', {})

    if quantity > 99:
        messages.error(
            request, 'Sorry, value must be less then or equal to 99.')
    elif quantity > 0:
        shopping_bag[item_id] = quantity
        messages.success(
            request, f'Updated {book.title}\
                 quantity to {shopping_bag[item_id]}')
    else:
        shopping_bag.pop(item_id)
        messages.success(request, f'Removed {book.title} from your bag')
    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('shopping_bag_view'))


def delete_from_shopping_bag(request, item_id):
    """ Removes item from bag """
    book = get_object_or_404(Book, pk=item_id)
    shopping_bag = request.session.get('shopping_bag', {})
    shopping_bag.pop(item_id)
    messages.success(request, f'Removed {book.title} from your bag')
    request.session['shopping_bag'] = shopping_bag
    return HttpResponse(status=200)
