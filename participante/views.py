from django.shortcuts import render
from .models import Participante

# # Create your views here.


def perfil(request, id):
     participante = Participante.objects.get(id=id)
     return render(request, 'participante/perfil.html', {"e":participante})