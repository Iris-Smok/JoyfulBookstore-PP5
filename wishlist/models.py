"""wishlist models"""
from django.db import models
from books.models import Book
from profiles.models import UserProfile


class Wishlist(models.Model):
    """ Wishlist model to store users favourite books"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                             related_name='user_wishlist',
                             null=False, blank=False)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.book.title
