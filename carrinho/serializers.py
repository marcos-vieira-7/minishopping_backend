from rest_framework import serializers
from .models import ItemCarrinho, Carrinho

class ItemCarrinhoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemCarrinho
        fields = "__all__"


class CarrinhoSerializer(serializers.ModelSerializer):
    itens = ItemCarrinhoSerializer(many=True)

    class Meta:
        model = Carrinho
        fields = "__all__"