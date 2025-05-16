from django.db import models

# Create your models here.
from django.db import models

class Imagem(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo