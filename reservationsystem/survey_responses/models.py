# Create your models here.
from django.db import models
from polls.models import Survey, Question, Choice

class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Response to {self.survey.name} on {self.submitted_at}'

class Answer(models.Model):
    response = models.ForeignKey(Response, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True)
    answer_date = models.DateField(blank=True, null=True)
    selected_choices = models.ManyToManyField(Choice, blank=True)

    def __str__(self):
        return f'Answer to {self.question.question_text} in response {self.response.id}'
