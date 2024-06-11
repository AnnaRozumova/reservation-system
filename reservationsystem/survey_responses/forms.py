from django import forms
from polls.models import Question

class DynamicSurveyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(DynamicSurveyForm, self).__init__(*args, **kwargs)

        for question in questions:
            field_name = f'question_{question.id}'
            if question.question_type == 'date':
                self.fields[field_name] = forms.DateField(label=question.question_text)
            elif question.question_type == 'email':
                self.fields[field_name] = forms.EmailField(label=question.question_text)
            elif question.question_type == 'single_choice':
                choices = [(choice.id, choice.choice_text) for choice in question.choices.all()]
                self.fields[field_name] = forms.ChoiceField(label=question.question_text, choices=choices, widget=forms.RadioSelect)
            elif question.question_type == 'multiple_choice':
                choices = [(choice.id, choice.choice_text) for choice in question.choices.all()]
                self.fields[field_name] = forms.MultipleChoiceField(label=question.question_text, choices=choices, widget=forms.CheckboxSelectMultiple)
