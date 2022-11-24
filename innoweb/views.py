from django.http import FileResponse
from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont
from score.models import Score
from django.contrib.auth import logout
from event.models import Event
from participant.models import Participant
from datetime import datetime

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


def certificate(request, event_id, participant_id):

    e = Event.objects.get(id=event_id)
    participant = Participant.objects.get(id=participant_id)

    score = Score.objects.get(event=e, participant=participant)


    certificate = Image.open("static\images\Sample_certificate.png")
    certificate.load()
    certificate = certificate.convert("RGB")


    new = ImageDraw.Draw(certificate)

    font = ImageFont.truetype(r"BRUSHSCI.TTF", 90)
    font_small = ImageFont.truetype(r"BRUSHSCI.TTF", 50)
    new.text((498, 518), participant.get_complete_name(), (0, 0, 0), font=font)
    new.text((757, 620), e.name, (0, 0, 0), font=font_small)
    new.text((560, 690), datetime.strftime(e.date, "%d/%m/%Y"), (0, 0, 0), font=font_small)
    new.text((890, 690), e.place, (0, 0, 0), font=font_small)
    new.text((1000, 757), str(score.value), (0, 0, 0), font=font_small)

    certificate.save("static\certificates\Certificado.pdf", "PDF", resolution=180.0)
    

    return FileResponse(open("static\certificates\Certificado.pdf", 'rb'), content_type='application/pdf')    