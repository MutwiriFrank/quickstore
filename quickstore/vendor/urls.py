from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet

router = DefaultRouter()
router.register(r"", VendorViewSet)  # Register the ProductViewSet

urlpatterns = [
    path("", include(router.urls)),  # Include the router's URLs
]
