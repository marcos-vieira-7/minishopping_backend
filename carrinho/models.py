from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto

# Create your models here.
class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(
        Carrinho,
        on_delete=models.CASCADE,
        related_name="itens"
    )

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)