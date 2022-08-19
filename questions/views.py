from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from . models import Question
from . forms import QuestionForm


def faq_page(request):
    """ FAQ's page view"""

    questions = Question.objects.all().filter(status=1).order_by('-created_on')
    context = {
        'questions': questions
    }
    template = 'questions/questions.html'

    return render(request, template, context)


def add_faq(request):
    """ Form for add questiona and answer """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added question & answer!')
            return redirect(reverse('add_faq'))
        else:
            messages.error(
                request, 'Failed to add question & answer. Please ensure the form is valid.')
    else:
        form = QuestionForm()
    template = 'questions/add_question.html'
    context = {
        'form': form
    }
    return render(request, template, context)
