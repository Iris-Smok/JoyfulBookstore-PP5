from django.contrib import admin
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    """ product model display """
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
    """category model dissplay"""
    list_display = (
        'friendly_name',
        'name'
    )

    search_fields = ('friendly_name', 'name',)


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
