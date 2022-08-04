from django.shortcuts import render, redirect


def shopping_bag_view(request):
    """ A view that render the shopping_bag content"""
    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ Add a quantity of the book to the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
        shopping_bag[item_id] = quantity

    request.session['shopping_bag'] = shopping_bag
    print(request.session['shopping_bag'])
    return(redirect(redirect_url))
