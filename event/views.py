from django.shortcuts import render
from .models import Event

# Create your views here.

def eventView(response, id):
    e = Event.objects.get(id=id)
    return render(response, "event/event_view.html", {"e": e})

