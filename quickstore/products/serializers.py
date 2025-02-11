from rest_framework import serializers
from .models import Product, Brand, Category, Variation, StoreToProduct


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
        fields = ['brand_id', 'brand_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name'] 


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = ['variation_id', 'variation', 'product']


class StoreToProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreToProduct
        fields = [
            'store_to_product_id',
            'product',
            'store',
            'product_price',
            'eff_start_date',
            'eff_end_date',
            'store_category'
        ] 