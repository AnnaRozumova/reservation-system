from django.urls import path
from . import views

app_name = 'survey_responses'
urlpatterns = [
    path('survey/<int:survey_id>/', views.survey_response_view, name='survey_response'),
    path('thank_you/', views.thank_you_view, name='thank_you'),
]