from django.shortcuts import render

from event.models import Event

# view for testing components
def index(request):
    return render(request, 'index.html')

def pruebaTablaParticipante(request):
    return render(request, 'tablaParticipante.html')

def home(request):

    events = Event.objects.all()

    # event = {
    #             "name": "Evento",
    #             "description": "Esto es un evento",
    #             "date": "2023-01-01",
    #             "place": "Lugar 1",
    #             "image": "https://picsum.photos/300/300/?random",
    #             "state": "Active",
    #         }

    # sample_events = [
    #     event, event, event, event, event, event, event, event, event
    # ]
    
    return render(request, 'base_HOME.html', {'events': events})
    

