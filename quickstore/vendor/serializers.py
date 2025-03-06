from rest_framework.serializers import ModelSerializer
from models import Vendor


class VendorSerializer(ModelSerializer):
    class Meta:
        model = Vendor
        exclude = [
            "created_at",
            "updated_at",
            "updated_by",
        ]
