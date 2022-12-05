from django.shortcuts import render
from .models import Participant
from score.models import Score
from django.contrib.messages import constants as messages

# # Create your views here.


def get_future_events(request):
          user = request.user
          future_events = Score.objects.filter(participant=user).filter(value=None).order_by('event__date')

          return [aux.event for aux in future_events]
          
     

def profile(request, id):

     def get_position(participant, event):
          scores = Score.objects.filter(event=event).order_by('-value').exclude(value=None)
          position = 1
          for score in scores:
               if score.participant == participant:
                    return position
               position += 1

     user = None
     my_profile = False
     if request.user.is_authenticated:
          user = request.user
          if user.id == id:
               my_profile = True

     p = Participant.objects.get(id=id)
     events_aux = Score.objects.filter(participant=p).order_by('-value').exclude(value=None)

     events = []
     total_points = 0
     n_events = 0

     for e in events_aux:
          event = {
               "id": e.event.id,
               'name': e.event.name,
               'points': e.value,
               'position': get_position(p, e.event)
          } 
          events.append(event)
          total_points += e.value
          n_events += 1
     
     future_events = []
     if my_profile:
          future_events = get_future_events(request)


     return render(request, 'base_PROFILE.html', {"participant":p ,"u_events":events, "total_points":total_points, "n_events":n_events, "my_profile":my_profile, "future_events":future_events})