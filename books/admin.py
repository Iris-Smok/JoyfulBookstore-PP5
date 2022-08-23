from django.contrib import admin
from .models import Book, Category, Review


class BookAdmin(admin.ModelAdmin):
    """ book model display """
    list_display = (
        'title',
        'category',
        'price',
        'review_count',
        'image'
    )

    search_fields = ('title', 'author', 'price',)
    ordering = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    """category model display"""
    list_display = (
        'friendly_name',
        'name'
    )

    search_fields = ('friendly_name', 'name',)


class ReviewAdmin(admin.ModelAdmin):
    """review model display"""
    list_display = (
        'user',
        'rating',
        'book',
        'created_on'

    )

    search_fields = ('user', 'book',)
    ordering = ('-created_on',)


admin.site.register(Review, ReviewAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
