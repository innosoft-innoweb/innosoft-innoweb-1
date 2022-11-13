from django.shortcuts import render
from .models import Score

import importlib

# Create your views here.

p = importlib.import_module("participant.models")
e = importlib.import_module("event.models")

def score_view(request, participant_id, event_id):

     participant = p.Participant.objects.get(id=participant_id)
     event = e.Event.objects.get(id=event_id)

     score = Score.objects.get(participant=participant, event=event)
     return render(request, 'score/score_view.html', {"e":score}) 