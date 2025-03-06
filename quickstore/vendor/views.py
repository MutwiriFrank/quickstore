from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    Vendor,
    Vendoremployee,
    Store,
    Storetocustomer,
    Supplier,
    Supplierproducttostoreorder,
    Supplierproducttostoreorderitem,
    Supplierstore,
    Supplierstoretoproduct,
)
from .serializers import (
    VendorSerializer,
    VendoremployeeSerializer,
    StoreSerializer,
    StoretocustomerSerializer,
    SupplierSerializer,
    SupplierproducttostoreorderSerializer,
    SupplierproducttostoreorderitemSerializer,
    SupplierstoreSerializer,
    SupplierstoretoproductSerializer,
)


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendoremployeeViewSet(viewsets.ModelViewSet):
    queryset = Vendoremployee.objects.all()
    serializer_class = VendoremployeeSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoretocustomerViewSet(viewsets.ModelViewSet):
    queryset = Storetocustomer.objects.all()
    serializer_class = StoretocustomerSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierproducttostoreorderViewSet(viewsets.ModelViewSet):
    queryset = Supplierproducttostoreorder.objects.all()
    serializer_class = SupplierproducttostoreorderSerializer


class SupplierproducttostoreorderitemViewSet(viewsets.ModelViewSet):
    queryset = Supplierproducttostoreorderitem.objects.all()
    serializer_class = SupplierproducttostoreorderitemSerializer


class SupplierstoreViewSet(viewsets.ModelViewSet):
    queryset = Supplierstore.objects.all()
    serializer_class = SupplierstoreSerializer


class SupplierstoretoproductViewSet(viewsets.ModelViewSet):
    queryset = Supplierstoretoproduct.objects.all()
    serializer_class = SupplierstoretoproductSerializer
