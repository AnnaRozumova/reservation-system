from django import forms
from polls.models import Event, RegistrantDetails, DetailsOfStay


VEG_MEAT_CHOICES = [
    ('veg', 'Vegetarian'),
    ('meat', 'Meat'),
]

CENTER_CHOICES = [
    ('Prague', 'Praha'),
    ('Brno', 'Brno'),
    ('Plzen', 'Plzen'),
]

TIME_OF_ARRIVING_CHOICES = [
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
    ('evening', 'Evening'),
]

STAY_OVERNIGHT_CHOICES = [
    ('yes', 'Yes'),
    ('no', 'No'),
]

class UserRegistrationForm(forms.Form):
    # Event selection
    event = forms.ModelChoiceField(queryset=Event.objects.all())

    # RegistrantDetails fields
    registrant_name = forms.CharField(max_length=200)
    registrant_surname = forms.CharField(max_length=200)
    registrant_veg_meat = forms.ChoiceField(choices=VEG_MEAT_CHOICES)
    registrant_email = forms.EmailField()
    registrant_center = forms.ChoiceField(choices=CENTER_CHOICES)

    # DetailsOfStay fields
    arriving = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time_of_arriving = forms.ChoiceField(choices=TIME_OF_ARRIVING_CHOICES)
    stay_overnight = forms.ChoiceField(choices=STAY_OVERNIGHT_CHOICES)
    departure = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))