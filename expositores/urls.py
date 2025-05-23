from django.urls import path
from . import views

app_name = 'expositores'

urlpatterns = [
    path('', views.lista_expositores, name='lista'),
    path('<slug:slug>/', views.detalhe_expositor, name='detalhe'),
    path('produto/<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
]