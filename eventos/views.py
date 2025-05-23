from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import Evento

def lista_eventos(request):
    agora = timezone.now()
    
    # Eventos futuros ordenados por data
    eventos_futuros = Evento.objects.filter(data__gte=agora).order_by('data')
    
    # Eventos passados ordenados por data decrescente
    eventos_passados = Evento.objects.filter(data__lt=agora).order_by('-data')
    
    context = {
        'eventos_futuros': eventos_futuros,
        'eventos_passados': eventos_passados,
    }
    
    return render(request, 'eventos/lista_eventos.html', context)