from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ category models """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Book(models.Model):
    """ book model """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254, null=True, blank=True)
    book_type = models.CharField(max_length=254, null=True, blank=True)
    book_size = models.CharField(max_length=254, null=True, blank=True)
    suitable_for_ages = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    likes = models.ManyToManyField(
        User,
        related_name='product_likes',
        blank=True
    )
    review_count = models.DecimalField(
        max_digits=6, decimal_places=0, null=True, blank=True, default=0
    )

    def __str__(self):
        return self.title
