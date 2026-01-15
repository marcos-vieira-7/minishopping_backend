from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Produto
from .serializers import ProdutoSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.
class ProdutoListCreateView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProdutoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAdminOrReadOnly]


"""
Isso cria:
GET /products/ → lista
POST /products/ → cria

GET /products/<id>/ → detalhe
PUT/PATCH /products/<id>/ → atualiza
DELETE /products/<id>/ → remove

"""