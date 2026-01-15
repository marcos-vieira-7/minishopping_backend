
from django.urls import path 
from .views import (
    ProdutoListCreateView,
    ProdutoRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("produtos/", ProdutoListCreateView.as_view()),
    path("produtos/<int:pk>", ProdutoRetrieveUpdateDestroyView.as_view()),
]

