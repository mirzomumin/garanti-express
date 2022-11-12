from django.shortcuts import render
from rest_framework import viewsets

from apps.products.product.models import Product, Color, ProductStock, Media
from apps.products.product.serializers import ProductSerializer, ColorSerializer, MediaSerializer, \
    ProductStockSerializer


# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ColorViewset(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ProductStockViewset(viewsets.ModelViewSet):
    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer


class MediaViewset(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
