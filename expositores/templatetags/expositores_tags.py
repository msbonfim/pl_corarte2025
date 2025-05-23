from django import template
from ..models import Expositor  # Importa o modelo Expositor

register = template.Library()

@register.inclusion_tag('expositores/partials/lista_expositores.html')
def mostrar_expositores(limit=6):
    """Renderiza uma lista de expositores"""
    expositores = Expositor.objects.filter(
        ativo=True
    ).order_by('-data_cadastro')[:limit]
    return {'expositores': expositores}