from django.shortcuts import render
from django.contrib.auth import logout

# view for testing components
def index(request):
    return render(request, 'index.html')

def home(request):

    if request.GET.get('logout') == 'logout':
       logout(request)

    event = {
                "name": "Evento",
                "description": "Esto es un evento",
                "date": "2023-01-01",
                "place": "Lugar 1",
                "image": "https://picsum.photos/300/300/?random",
                "state": "Active",
            }

    sample_events = [
        event, event, event, event, event, event, event, event, event
    ]
    
    return render(request, 'base_HOME.html', {'events': sample_events})
    

