from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'criado_em')
    list_filter = ('data',)
    search_fields = ('titulo', 'descricao')
    date_hierarchy = 'data'
    ordering = ('-data',)