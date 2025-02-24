from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Retrieve all products
    serializer_class = ProductSerializer  # Use the ProductSerializer
    
    
