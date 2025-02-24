from rest_framework import serializers
from .models import Product, Brand, Category, Variation, Storetoproduct, Storecategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "product_id",
            "country",
            "product_name",
            "category",
            "brand",
            "product_description",
            "is_digital",
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["brand_id", "brand_name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category_id", "category_name"]


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = ["variation_id", "variation", "product"]


class StorecategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Storecategory
        fields = [
            "store_category_id",
            "store_category_name",
            "category",  # ForeignKey to Category
        ]


class StoretoproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storetoproduct
        fields = [
            "store_to_product_id",
            "product",  # ForeignKey to Product
            "store",  # ForeignKey to Store
            "product_price",
            "eff_start_date",
            "eff_end_date",
            "store_category",  # ForeignKey to Storecategory
        ]
