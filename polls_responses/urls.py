from django.urls import path
from polls_responses.views import event_detail, registrant_details


urlpatterns = [
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('event/<int:event_id>/registrant/<int:registrant_id>/', registrant_details, name='registrant_details'),
]