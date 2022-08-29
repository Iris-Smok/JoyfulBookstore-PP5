from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Subscriber, SubscriberEmail


class SubscriberAdmin(admin.ModelAdmin):
    """ Subscriber model display """
    list_display = (
        'email', 'date'
    )

    search_fields = ('email', 'date')
    ordering = ('date',)


class SubscriberEmailAdmin(SummernoteModelAdmin):
    """ Email model display """
    list_display = (
        'title',
    )

    search_fields = ('title', 'message')


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(SubscriberEmail, SubscriberEmailAdmin)
