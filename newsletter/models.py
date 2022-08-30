from django.db import models


class Subscriber(models.Model):
    """ model to store subscriber email"""
    subscriber_email = models.EmailField(
        max_length=254, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class SubscriberEmail(models.Model):
    """ model to store newsletter """
    title = models.CharField(max_length=254, null=False, blank=False)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
