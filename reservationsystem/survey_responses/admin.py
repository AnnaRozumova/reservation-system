# Register your models here.
from django.contrib import admin
from .models import Response, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

class ResponseAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('survey', 'submitted_at')
    list_filter = ('survey', 'submitted_at')

admin.site.register(Response, ResponseAdmin)
admin.site.register(Answer)