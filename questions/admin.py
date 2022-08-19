from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    """ Question model display """
    list_display = (
        'question', 'answer', 'status', 'created_on'
    )

    search_fields = ('question', 'answer')
    ordering = ('created_on',)


admin.site.register(Question, QuestionAdmin)
