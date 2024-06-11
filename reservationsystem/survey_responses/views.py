# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from polls.models import Survey, Question, Choice
from .models import Response, Answer
from .forms import DynamicSurveyForm

def survey_response_view(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id, is_active=True)
    questions = survey.questions.all()

    if request.method == 'POST':
        form = DynamicSurveyForm(request.POST, questions=questions)
        if form.is_valid():
            response = Response.objects.create(survey=survey)
            for question in questions:
                question_id = f'question_{question.id}'
                if question.question_type == 'date':
                    answer_date = form.cleaned_data[question_id]
                    Answer.objects.create(response=response, question=question, answer_date=answer_date)
                elif question.question_type == 'email':
                    answer_text = form.cleaned_data[question_id]
                    Answer.objects.create(response=response, question=question, answer_text=answer_text)
                elif question.question_type == 'single_choice':
                    choice_id = form.cleaned_data[question_id]
                    choice = Choice.objects.get(id=choice_id)
                    answer = Answer.objects.create(response=response, question=question)
                    answer.selected_choices.add(choice)
                elif question.question_type == 'multiple_choice':
                    choice_ids = form.cleaned_data[question_id]
                    choices = Choice.objects.filter(id__in=choice_ids)
                    answer = Answer.objects.create(response=response, question=question)
                    answer.selected_choices.set(choices)
            return redirect('survey_responses:thank_you')
    else:
        form = DynamicSurveyForm(questions=questions)

    return render(request, 'survey_responses/survey_response_form.html', {'form': form, 'survey': survey})


def thank_you_view(request):
    return render(request, 'survey_responses/thank_you.html')