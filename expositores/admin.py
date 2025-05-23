from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Expositor, CategoriaProduto, Produto

class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 1
    fields = ('nome', 'descricao', 'preco', 'destaque')

@admin.register(Expositor)
class ExpositorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome', 'descricao')
    prepopulated_fields = {'slug': ('nome',)}
    inlines = [ProdutoInline]

@admin.register(CategoriaProduto)
class CategoriaProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'expositor', 'preco', 'destaque')
    list_filter = ('expositor', 'categoria', 'destaque')
    search_fields = ('nome', 'descricao')
    list_editable = ('destaque',)