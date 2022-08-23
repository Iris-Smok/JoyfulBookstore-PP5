""" Get wishlist items """

from .models import Wishlist
from profiles.models import UserProfile


def wishlist_list_items(request):
    """ wishlist items """
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        list_to_display = []
        wishlist_content = Wishlist.objects.filter(user=user)
        # if there are items in the users wishlist
        for item in wishlist_content:
            # append the item to list to display
            list_to_display.append(item.book)
    else:
        list_to_display = []
    return {
        'wishlist_items': list_to_display,
    }
