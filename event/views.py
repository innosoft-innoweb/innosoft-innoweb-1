from django.shortcuts import render
from .models import Event
from score.models import Score

def event_view(response, id):

    e = Event.objects.get(id=id)

    scores = Score.objects.filter(event=e).order_by('-value')

    first = None
    second = None
    third = None

    if len(scores) > 0:
        if len(scores) >= 3:
            third = scores[2].participant
            third.name = third.get_short()
        if len(scores) >= 2:
            second = scores[1].participant
            second.name = second.get_short()
        if len(scores) >= 1:
            first = scores[0].participant
            first.name = first.get_short()

    e.date = e.date.strftime("%d/%m/%Y a las %H:%M")

    return render(response, "base_EVENT.html", {
        "e": e, 
        "scores": scores,
        "first": first,
        "second": second,
        "third": third
        })
