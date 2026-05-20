from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Produto
from .serializers import ProdutoSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

# below create generic views for list, create, retrieve, update and destroy
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [AllowAny]

class ProdutoListView(viewsets.ReadOnlyModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [AllowAny]


"""
Isso cria:
GET /products/ → lista
POST /products/ → cria

GET /products/<id>/ → detalhe
PUT/PATCH /products/<id>/ → atualiza
DELETE /products/<id>/ → remove

"""