from rest_framework import serializers
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


# Serializers
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        exclude = ("created_at", "updated_at")


class VendoremployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendoremployee
        exclude = ("created_at", "updated_at")


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        exclude = ("created_at", "updated_at")


class StoretocustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storetocustomer
        exclude = ("created_at", "updated_at")


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        exclude = ("created_at", "updated_at")


class SupplierproducttostoreorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplierproducttostoreorder
        exclude = ("created_at", "updated_at")


class SupplierproducttostoreorderitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplierproducttostoreorderitem
        exclude = ("created_at", "updated_at")


class SupplierstoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplierstore
        exclude = ("created_at", "updated_at")


class SupplierstoretoproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplierstoretoproduct
        exclude = ("created_at", "updated_at")
