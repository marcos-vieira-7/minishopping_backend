from django.shortcuts import render
from rest_framework import viewsets

from .models import Carrinho, ItemCarrinho
from .serializers import (
    CarrinhoSerializer,
    ItemCarrinhoSerializer
)


class CarrinhoViewSet(viewsets.ModelViewSet):

    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer


class ItemCarrinhoViewSet(viewsets.ModelViewSet):

    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer
