from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pruebaTablaParticipante(request):
    return render(request, 'tablaParticipante.html')