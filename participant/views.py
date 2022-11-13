from django.shortcuts import render
from .models import Participant

# # Create your views here.


def profile(request, id):
     participant = Participant.objects.get(id=id)
     return render(request, 'participant/profile.html', {"e":participant}) #participant/perfil.html is the path of templates