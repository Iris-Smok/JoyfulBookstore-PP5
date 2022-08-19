""" FAQ's model"""
from django.db import models

STATUS_CHOICES = ((0, "Draft"), (1, "Published"))


class Question(models.Model):
    """ Model to store FAQ's"""
    question = models.CharField(max_length=254, blank=False, null=False)
    answer = models.TextField()
    created_on = models.DateTimeField(auto_now=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        """
        orders the questions by date when it was created,
        the most recent first
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.status} {self.question}"
