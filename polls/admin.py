from django.contrib import admin
from polls.models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    fields = ('title', 'date', 'description', 'contact_person')


admin.site.register(Event, EventAdmin)