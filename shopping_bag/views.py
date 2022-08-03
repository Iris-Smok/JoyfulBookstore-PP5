from django.shortcuts import render


def shopping_bag(request):
    return render(request, 'shopping_bag/shopping_bag.html')
