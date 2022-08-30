""" models for Category,Book """
from django.db import models
from profiles.models import UserProfile


class Category(models.Model):
    """ category models """
    class Meta:
        """ add correct plural name"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """method to get category friendly name"""
        return str(self.friendly_name)


class Book(models.Model):
    """ book model """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    is_new = models.BooleanField(default=True)
    book_type = models.CharField(max_length=254, null=True, blank=True)
    book_size = models.CharField(max_length=254, null=True, blank=True)
    suitable_for_ages = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    review_count = models.DecimalField(
        max_digits=6, decimal_places=0, null=True, blank=True, default=0
    )
    sort_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if self.sale_price:
            self.sort_price = self.sale_price
        else:
            self.sort_price = self.price
        return super(Book, self).save(*args, **kwargs)


class Review(models.Model):
    """ A review model for users to review books """

    RATING = [
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING, default=3)
    body = models.TextField(max_length=1024)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.user} rated {self.book}, {self.book} stars.'
