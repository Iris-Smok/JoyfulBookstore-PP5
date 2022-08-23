""" Get wishlist items """
from .models import Wishlist
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile


@login_required
def wishlist_list(request):
    """ wishlist items """
    user = UserProfile.objects.get(user=request.user)
    wishlist_list = Wishlist.objects.filter(user=user)
    list_to_display = []
    for item in wishlist_list:
        list_to_display.append(item.book)

    return {
        'wishlist_items': list_to_display,
    }
