from django.contrib import admin
from .models import Subscriber, SubscriberEmail


class SubscriberAdmin(admin.ModelAdmin):
    """ Subscriber model display """
    list_display = (
        'subscriber_email', 'date'
    )

    search_fields = ('subscriber_email', 'date')
    ordering = ('date',)


class SubscriberEmailAdmin(admin.ModelAdmin):
    """ Email model display """
    list_display = (
        'title',
    )

    search_fields = ('title', 'message')


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(SubscriberEmail, SubscriberEmailAdmin)
