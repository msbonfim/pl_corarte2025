from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator

class Expositor(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    descricao = models.TextField(validators=[MinLengthValidator(50)])
    logo = models.ImageField(upload_to='expositores/logos/')
    website = models.URLField(blank=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Expositor'
        verbose_name_plural = 'Expositores'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class CategoriaProduto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Categoria de Produto'
        verbose_name_plural = 'Categorias de Produtos'

    def __str__(self):
        return self.nome

class Produto(models.Model):
    expositor = models.ForeignKey(Expositor, on_delete=models.CASCADE, related_name='produtos')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.ForeignKey(CategoriaProduto, on_delete=models.SET_NULL, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/imagens/')
    destaque = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-destaque', 'nome']

    def __str__(self):
        return f"{self.nome} ({self.expositor.nome})"