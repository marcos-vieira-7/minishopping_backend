from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from produtos.models import Produto

from .models import Carrinho, ItemCarrinho
from .serializers import (
    CarrinhoSerializer,
    ItemCarrinhoSerializer
)

class CarrinhoViewSet(viewsets.ModelViewSet):

    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def meu_carrinho(self, request):
        carrinho, criado = Carrinho.objects.get_or_create(usuario=request.user)
        serializer = self.get_serializer(carrinho)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def adicionar_item(self, request):


        produto_id = request.data.get("produto_id")
        quantidade = request.data.get("quantidade", 1)

        try:
            produto = Produto.objects.get(id=produto_id)

        except Produto.DoesNotExist:

            return Response(
                {"erro": "Produto não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )

        carrinho, criado = Carrinho.objects.get_or_create(
            usuario=request.user
        )

        item_existente = ItemCarrinho.objects.filter(
            carrinho=carrinho,
            produto=produto
        ).first()

        if item_existente:

            item_existente.quantidade += int(quantidade)
            item_existente.save()

        else:

            ItemCarrinho.objects.create(
                carrinho=carrinho,
                produto=produto,
                quantidade=quantidade,
                preco=produto.preco
            )

        return Response({
            "ok": True
        })


class ItemCarrinhoViewSet(viewsets.ModelViewSet):

    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer
