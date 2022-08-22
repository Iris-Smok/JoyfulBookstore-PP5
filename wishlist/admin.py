from django.contrib import admin
from . models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    model = Wishlist
    fields = ('user', 'book')
    list_display = ('pk', 'user', 'book')


admin.site.register(Wishlist, WishlistAdmin)
