from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_faq(request):
    """ Form for add questiona and answer """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    questions = Question.objects.all()

    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added FAQ!')
            return redirect(reverse('add_faq'))
        else:
            messages.error(
                request, 'Failed to add FAQ. Please ensure the form is valid.')
    else:
        form = QuestionForm()
    template = 'questions/add_question.html'
    context = {
        'form': form,
        'questions': questions,
        'on_page': True
    }
    return render(request, template, context)


@login_required
def edit_faq(request, question_id):
    """ Edit a faq on faq page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))

    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated FAQ!')
            return redirect(reverse('add_faq'))
        else:
            messages.error(
                request,
                'Failed to update FAQ. Please ensure the form is valid.')
    else:
        form = QuestionForm(instance=question)
        messages.info(request, f'You are editing {question.question}')

    template = 'questions/edit_question.html'
    context = {
        'form': form,
        'question': question,
        'on_page': True
    }

    return render(request, template, context)


@login_required
def delete_faq(request, question_id):
    """ Delete FAQ"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that.')
        return redirect(reverse('home'))
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    messages.success(request, 'FAQ deleted')

    return redirect(reverse('add_faq'))
