from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2) #dinheiro nunca use float.
    estoque = models.PositiveIntegerField()
    categoria = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

