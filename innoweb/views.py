from django.shortcuts import render
from score.models import Score

# view for testing components
def index(request):
    return render(request, 'index.html')

def home(request):

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

    scores = Score.objects.order_by('-value')
    first = scores[0].participant
    first.surname = first.surname[0] + '.'
    second = scores[1].participant
    second.surname = second.surname[0] + '.'
    third = scores[2].participant
    third.surname = third.surname[0] + '.'



    
    return render(request, 'base_HOME.html', 
        {'events': sample_events,
        'first': first,
        'second': second,
        'third': third
        })
    
