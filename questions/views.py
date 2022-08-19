from django.shortcuts import render, get_object_or_404
from . models import Question


def faq_page(request):
    """ FAQ's page view"""

    questions = Question.objects.all().filter(status=1).order_by('-created_on')
    context = {
        'questions': questions
    }
    template = 'questions/questions.html'

    return render(request, template, context)
