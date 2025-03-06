from rest_framework import viewsets
from .models import Product, Brand, Category, Variation, Storecategory, Storetoproduct
from .serializers import (
    ProductSerializer,
    BrandSerializer,
    CategorySerializer,
    VariationSerializer,
    StorecategorySerializer,
    StoretoproductSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Retrieve all products
    serializer_class = ProductSerializer  # Use the ProductSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()  # Retrieve all products
    serializer_class = BrandSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # Retrieve all products
    serializer_class = CategorySerializer  # Use the ProductSerializer


class VariationViewSet(viewsets.ModelViewSet):
    queryset = Variation.objects.all()  # Retrieve all products
    serializer_class = VariationSerializer


class StorecategoryViewSet(viewsets.ModelViewSet):
    queryset = Storecategory.objects.all()  # Retrieve all products
    serializer_class = StorecategorySerializer  # Use the ProductSerializer


class StoretoproductViewSet(viewsets.ModelViewSet):
    queryset = Storetoproduct.objects.all()  # Retrieve all products
    serializer_class = StoretoproductSerializer
