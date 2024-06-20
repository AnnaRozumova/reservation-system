from django.urls import path
from polls.views import home, user_registration_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path('register/', user_registration_view, name='user_registration'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]
