from django.shortcuts import render
from .models import Imagem

def lista_imagens(request):
    imagens = Imagem.objects.all().order_by('-criado_em')
    return render(request, 'galeria/galeria.html', {'imagens': imagens})

from galeria.models import Imagem  # importa o model de imagens

def home(request):
    imagens = Imagem.objects.all().order_by('-criado_em')
    return render(request, 'home/home.html', {'imagens': imagens})