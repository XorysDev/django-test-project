from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
