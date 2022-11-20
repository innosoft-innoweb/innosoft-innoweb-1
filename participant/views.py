from django.shortcuts import render
from .models import Participant

# # Create your views here.



def profile(request, id):
     participant = Participant.objects.get(id=id)

     event = {
                "name": "Evento",
                "position": "3",
                "points": "81"
            }

     sample_events = [
          event, event, event
     ]

     print(sample_events)

     return render(request, 'participant/profile.html', {"u_events":sample_events}) #participant/perfil.html is the path of templates