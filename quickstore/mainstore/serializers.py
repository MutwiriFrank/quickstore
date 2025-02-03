from rest_framework import serializers


from . import models


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['vendor_id', 'tenant', 'user', 'country', 'vendor_name', 'phone_number']