from django.shortcuts import render
from score.models import Score
from django.contrib.auth import logout


from event.models import Event

# view for testing components
def index(request):
    return render(request, 'index.html')

def home(request):
    
    events = Event.objects.filter(status='Abierto')
    
    if request.GET.get('logout') == 'logout':
       logout(request)
    
    user = None
    if request.user.is_authenticated:
        user = request.user


    
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
            third.username = third.get_username()
        
        if len(participants) >= 2:
            second = participants[1]
            second.username = second.get_username()
        
        if len(participants) >= 1:
            first = participants[0]
            first.username = first.get_username()

    return render(request, 'base_HOME.html', 
        {'events': events,
        'first': first,
        'second': second,
        'third': third
        })

