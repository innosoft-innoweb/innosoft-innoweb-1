from django.shortcuts import render, redirect
from .models import Event
from score.models import Score
from django.contrib import messages

def event_view(request, id):

    e = Event.objects.get(id=id)

    scores = Score.objects.filter(event=e).order_by('-value').exclude(value=None)

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

    return render(request, "base_EVENT.html", {
        "e": e, 
        "scores": scores,
        "first": first,
        "second": second,
        "third": third
        })

def join_event(request, id):
    if request.user.is_authenticated:
        event = Event.objects.get(id=id)
        scores = Score.objects.filter(event=event)
        # if the user is not in the scores
        if not scores.filter(participant=request.user).exists():
            score = Score(participant=request.user, event=event, value=None) # create a new score with value null
            score.save()
            messages.success(request, 'Te has unido al evento correctamente')
        
        else:
            messages.warning(request, 'Ya estás inscrito en el evento')
        
        
    else:
        messages.error(request, 'Debes iniciar sesión para unirte a un evento')
    
    return redirect('event', id=id)