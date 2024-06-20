from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class RegistrantDetails(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    veg_meat = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    center = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE) 

class DetailsOfStay(models.Model):
    arriving = models.DateField()
    time_of_arriving = models.CharField(max_length=100)
    stay_overnight = models.CharField(max_length=100)
    departure = models.DateField()
    registrant = models.ForeignKey(RegistrantDetails, on_delete=models.CASCADE)




