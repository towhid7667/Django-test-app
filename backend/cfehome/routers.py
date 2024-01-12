from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSets, ProductGenericViewSet

router = DefaultRouter()

router.register('products-abc', ProductViewSets, basename='products')
router.register('products', ProductGenericViewSet, basename='products')
urlpatterns=router.urls