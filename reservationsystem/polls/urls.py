from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.SurveyDetailView.as_view(), name='detail'),
]

