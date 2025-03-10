from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeliveryViewSet, OrderitemViewSet, OrdersViewSet, WishlistViewSet

router = DefaultRouter()

router.register(r"deliveries", DeliveryViewSet)
router.register(r"orderitems", OrderitemViewSet)
router.register(r"orders", OrdersViewSet)
router.register(r"wishlists", WishlistViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
