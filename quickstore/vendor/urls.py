from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VendorViewSet,
    VendoremployeeViewSet,
    StoreViewSet,
    StoretocustomerViewSet,
    SupplierViewSet,
    SupplierproducttostoreorderViewSet,
    SupplierproducttostoreorderitemViewSet,
    SupplierstoreViewSet,
    SupplierstoretoproductViewSet,
)

router = DefaultRouter()
router.register(r"vendors", VendorViewSet)
router.register(r"vendoremployees", VendoremployeeViewSet)
router.register(r"stores", StoreViewSet)
router.register(r"storetocustomers", StoretocustomerViewSet)
router.register(r"suppliers", SupplierViewSet)
router.register(r"supplierorders", SupplierproducttostoreorderViewSet)
router.register(r"supplierorderitems", SupplierproducttostoreorderitemViewSet)
router.register(r"supplierstores", SupplierstoreViewSet)
router.register(r"supplierstoreproducts", SupplierstoretoproductViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
