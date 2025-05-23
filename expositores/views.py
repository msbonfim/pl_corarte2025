from django.shortcuts import render, get_object_or_404
from .models import Expositor, Produto, CategoriaProduto

# Create your views here.

def lista_expositores(request):
    expositores = Expositor.objects.filter(ativo=True).order

    from django.shortcuts import render, get_object_or_404
from .models import Expositor, Produto

def lista_expositores(request):
    expositores = Expositor.objects.filter(ativo=True).order_by('nome')
    context = {
        'expositores': expositores,
        'titulo': 'Nossos Expositores'
    }
    return render(request, 'expositores/lista.html', context)

def detalhe_expositor(request, slug):
    expositor = get_object_or_404(Expositor, slug=slug, ativo=True)
    produtos = expositor.produtos.all()
    
    context = {
        'expositor': expositor,
        'produtos': produtos,
        'titulo': f"Expositor - {expositor.nome}"
    }
    return render(request, 'expositores/detalhe.html', context)

def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    
    context = {
        'produto': produto,
        'titulo': f"Produto - {produto.nome}"
    }
    return render(request, 'expositores/produto.html', context)