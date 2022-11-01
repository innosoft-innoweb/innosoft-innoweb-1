from django.shortcuts import render
from .models import Participant

# # Create your views here.


def perfil(request, id):
     participant = Participant.objects.get(id=id)
     return render(request, 'participant/perfil.html', {"e":participant}) #participant/perfil.html is the path of templates