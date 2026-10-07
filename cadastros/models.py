from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

def __str__(self):
    return self.nome