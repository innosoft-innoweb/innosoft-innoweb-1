from django.shortcuts import render
from .models import Evento

# Create your views here.

def vistaEvento(response, id):
    e = Evento.objects.get(id=id)
    return render(response, "evento/vista_evento.html", {"e": e})

