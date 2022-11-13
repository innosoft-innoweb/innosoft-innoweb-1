from django.shortcuts import render
from .models import Event
from score.models import Score


# Create your views here.

def eventView(response, id):
    e = Event.objects.get(id=id)
    
    scores = Score.objects.filter(event=e).order_by('-value')
    return render(response, "event/event_view.html", {
        "e": e, 
        "scores": scores
        })

