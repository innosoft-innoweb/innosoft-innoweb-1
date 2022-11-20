from django.shortcuts import render

from event.models import Event

# view for testing components
def index(request):
    return render(request, 'index.html')

def pruebaTablaParticipante(request):
    return render(request, 'tablaParticipante.html')

def home(request):

    
    events = Event.objects.filter(status='Abierto')
    
    return render(request, 'base_HOME.html', {'events': events})
    

