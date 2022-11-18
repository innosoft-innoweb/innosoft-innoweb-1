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

    first = None
    second = None
    third = None
    
    if len(scores) > 0:
        scores_dict = {}
        for score in scores:
            if score.participant in scores_dict:
                scores_dict[score.participant] += score.value
            else:
                scores_dict[score.participant] = score.value

        
        participants = sorted(scores_dict, key=scores_dict.get, reverse=True)

        if len(participants) >= 3:
            third = participants[2]
            third.name = third.get_short()
        
        if len(participants) >= 2:
            second = participants[1]
            second.name = second.get_short()
        
        if len(participants) >= 1:
            first = participants[0]
            first.name = first.get_short()

    return render(request, 'base_HOME.html', 
        {'events': sample_events,
        'first': first,
        'second': second,
        'third': third
        })
