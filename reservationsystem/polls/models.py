# Create your models here. Those models are covering only formes of surveys. Choices of users will be done in another application
from django.db import models

class Question(models.Model):
    QUESTION_TYPES = [
        ('date', 'Date'),
        ('email', 'Email'),
        ('single_choice', 'Single Choice'),
        ('multiple_choice', 'Multiple Choice'),
    ]

    question_text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

class Survey(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    questions = models.ManyToManyField(Question, through='SurveyQuestion')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class SurveyQuestion(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('survey', 'question')
        ordering = ['order']