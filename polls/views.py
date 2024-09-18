from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from polls.forms import UserRegistrationForm
from polls.models import Event, RegistrantDetails, DetailsOfStay

# Create your views here.

def home(request):
    events = Event.objects.all()
    return render(request, 'polls/home.html', {'events': events})

def user_registration_view(request):
    event_id = request.GET.get('event_id')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            event = form.cleaned_data['event']
            
            # Create RegistrantDetails instance
            registrant = RegistrantDetails.objects.create(
                name=form.cleaned_data['registrant_name'],
                surname=form.cleaned_data['registrant_surname'],
                veg_meat=form.cleaned_data['registrant_veg_meat'],
                email=form.cleaned_data['registrant_email'],
                center=form.cleaned_data['registrant_center'],
                event=event
            )
            # Create DetailsOfStay instance
            DetailsOfStay.objects.create(
                arriving=form.cleaned_data['arriving'],
                time_of_arriving=form.cleaned_data['time_of_arriving'],
                stay_overnight=form.cleaned_data['stay_overnight'],
                departure=form.cleaned_data['departure'],
                registrant=registrant
            )

            registrant_detail_url = request.build_absolute_uri(
                reverse('registrant_details', args=[event.id, registrant.id])
            )

            subject = 'Your Tenovice Registration Confirmation'
            message = f'Dear {registrant.name},\n\nThank you for registering for the event "{event.title}". You can view your registration details at the following link:\n\n{registrant_detail_url}\n\nBest regards,\nYour Tenovice Team'
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [registrant.email],
                fail_silently=False,
            )

            return render(request, 'polls/success.html', {'registrant_detail_url': registrant_detail_url})  # Redirect to a success page
    else:
        if event_id:
            event = get_object_or_404(Event, id=event_id)
            form = UserRegistrationForm(initial={'event': event})
        else:
            form = UserRegistrationForm()

    return render(request, 'polls/user_registration_form.html', {'form': form})
