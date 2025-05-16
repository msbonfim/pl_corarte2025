from django.urls import path
from . import views  # Importa as views do próprio app

app_name = 'eventos'  # Namespace opcional

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
]