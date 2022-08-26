from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from . models import Wishlist
from books.models import Book


@login_required
def wishlist(request):
    """ wishlist page """

    template = 'wishlist/wishlist.html'
    context = {
        'on_page': True,
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, book_id):
    """ View to add book to wishlist"""
    user = UserProfile.objects.get(user=request.user)
    book = get_object_or_404(Book, pk=book_id)
    wishlist_exists = Wishlist.objects.filter(user=user, book=book).exists()

    if wishlist_exists:
        wishlist_item = Wishlist.objects.get(
            user=user,
            book=book
        )
        wishlist_item.delete()
        messages.info(request, 'Removed from wishlist')
        return redirect(reverse('book_detail', args=[book.id]))
    else:
        wishlist_item = Wishlist.objects.create(
            user=user,
            book=book
        )
        messages.success(
            request, f'Successfully added {wishlist_item} to wishlist')
        return redirect(reverse('book_detail', args=[book.id]))


@login_required
def remove_from_wishlist(request, book_id):
    """ Remove from wishlist"""
    user = UserProfile.objects.get(user=request.user)
    book = get_object_or_404(Book, pk=book_id)
    wishlist_item = Wishlist.objects.get(user=user, book=book)
    wishlist_item.delete()
    messages.success(request, f'Successfully removed {book.title}')
    return redirect(reverse('wishlist'))
