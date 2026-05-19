from rest_framework.routers import DefaultRouter

from .views import (
    CarrinhoViewSet,
    ItemCarrinhoViewSet
)

router = DefaultRouter()

router.register(r'carrinhos', CarrinhoViewSet)
router.register(r'itens-carrinho', ItemCarrinhoViewSet)

urlpatterns = router.urls