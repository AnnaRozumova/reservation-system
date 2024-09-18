from django.shortcuts import render, get_object_or_404
from polls.models import Event, RegistrantDetails, DetailsOfStay

# Create your views here.
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    registrants = RegistrantDetails.objects.filter(event=event)

    stay_details = DetailsOfStay.objects.filter(registrant__in=registrants)

    context = {
        'event' : event,
        'registrants' : registrants,
        'stay_details' : stay_details,
    }

    return render(request, 'polls_responses/event_detail.html', context)


def registrant_details(request, event_id, registrant_id):
    event = get_object_or_404(Event, id=event_id)
    registrant = get_object_or_404(RegistrantDetails, id=registrant_id, event=event)
    stay_details = DetailsOfStay.objects.filter(registrant=registrant)

    context = {
        'event': event,
        'registrant': registrant,
        'stay_details': stay_details,
    }

    return render(request, 'polls_responses/registrant_details.html', context)