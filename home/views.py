from django.shortcuts import render
from django.http import HttpResponse
from galeria.models import Imagem
from eventos.models import Evento
from django.utils import timezone
from expositores.models import Expositor
from django.db import connection  # Adicionado para debug


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
    return render(request, 'home/index.html', context)


def home(request):
    # Pegar os 6 expositores mais recentes ou destacados
    expositores_destaque = Expositor.objects.filter(ativo=True).order_by('-data_cadastro')[:6]
    
    context = {
        'expositores_destaque': expositores_destaque,
    }
    return render(request, 'home/index.html', context)



def home(request):
    try:
        # Debug 1: Verificar conexão com o banco
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM expositores_expositor")
            total_db = cursor.fetchone()[0]
        
        # Debug 2: Verificar consulta ORM
        total_orm = Expositor.objects.count()
        expositores = Expositor.objects.filter(ativo=True).exclude(logo__exact='')
        
        context = {
            'expositores_destaque': expositores[:6],
            'debug_data': {
                'total_db': total_db,
                'total_orm': total_orm,
                'filtrados': expositores.count(),
                'query': str(expositores.query),
            }
        }
        
        # Debug no console
        print("\n=== DEBUG VIEW ===")
        print(f"Total no DB (raw): {total_db}")
        print(f"Total no ORM: {total_orm}")
        print(f"Filtrados: {expositores.count()}")
        print(f"Query: {expositores.query}\n")
        
    except Exception as e:
        context = {
            'expositores_destaque': [],
            'debug_data': {
                'error': str(e),
                'type': type(e).__name__
            }
        }
        print(f"\n=== ERRO NA VIEW ===\n{str(e)}\n")
    
    return render(request, 'home/index.html', context)