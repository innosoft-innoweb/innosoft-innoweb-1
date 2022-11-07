from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
  
def events_list(request):

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

    return render(request, 'components\events_list.html', {'events': sample_events})
    
