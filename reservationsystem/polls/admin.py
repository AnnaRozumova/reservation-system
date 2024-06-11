# Register your models here.
from django.contrib import admin

from .models import Survey, Question, Choice, SurveyQuestion

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class SurveyQuestionInline(admin.TabularInline):
    model = SurveyQuestion
    extra = 1

class SurveyAdmin(admin.ModelAdmin):
    inlines = [SurveyQuestionInline]
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(SurveyQuestion)