from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet,
    CategoryViewSet,
    VariationViewSet,
    BrandViewSet,
    StorecategoryViewSet,
    StoretoproductViewSet,
)

router = DefaultRouter()
router.register(r"product", ProductViewSet)  # Register the ProductViewSet
router.register(r"category", CategoryViewSet)
router.register(r"brand", BrandViewSet)
router.register(r"variation", VariationViewSet)
router.register(r"storeProduct", StoretoproductViewSet)
router.register(r"storeCategory", StorecategoryViewSet)


urlpatterns = [
    path("", include(router.urls)),  # Include the router's URLs
]
