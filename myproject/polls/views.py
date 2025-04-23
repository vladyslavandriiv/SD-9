from django.shortcuts import render

from polls.models import Question


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'polls/question_list.html', {'questions': questions})
