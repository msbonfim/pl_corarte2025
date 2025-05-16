from django.shortcuts import render
from django.http import HttpResponse
from galeria.models import Imagem
from eventos.models import Evento
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'index.html')

def index(request):
    imagens = Imagem.objects.all().order_by('-criado_em')  # pega as imagens
    return render(request, 'home/index.html', {'imagens': imagens})
    
def home(request):
    agora = timezone.now()
    context = {
        'eventos_futuros': Evento.objects.filter(data__gte=agora).order_by('data')[:3],
        'eventos_passados': Evento.objects.filter(data__lt=agora).order_by('-data')[:3]
    }
    return render(request, 'home.html', context)