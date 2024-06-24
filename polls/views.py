from django.shortcuts import render, redirect
from polls.forms import UserRegistrationForm
from polls.models import Event, RegistrantDetails, DetailsOfStay

# Create your views here.

def home(request):
    return render(request, 'polls/home.html')

def user_registration_view(request):
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
            return redirect('success')  # Redirect to a success page
    else:
        form = UserRegistrationForm()

    return render(request, 'polls/user_registration_form.html', {'form': form})
