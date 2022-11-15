from django.shortcuts import render
from .models import Event
from score.models import Score


# Create your views here.

def eventView(response, id):
    e = Event.objects.get(id=id)
    
    scores = Score.objects.filter(event=e).order_by('-value')
    first = scores[0].participant
    first.surname = first.surname[0] + '.'
    second = scores[1].participant
    second.surname = second.surname[0] + '.'
    third = scores[2].participant  
    third.surname = third.surname[0] + '.' 
    return render(response, "event/event_view.html", {
        "e": e, 
        "scores": scores,
        "first": first,
        "second": second,
        "third": third
        })

