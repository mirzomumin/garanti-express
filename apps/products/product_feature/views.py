from django.shortcuts import render
from rest_framework import viewsets

from apps.products.product_feature.models import Feature, FeatureElement, ProductFeature
from apps.products.product_feature.serializers import FeatureSerializer, FeatureElementSerializer, \
    ProductFeatureSerializer


# Create your views here.

class FeatureViewset(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class FeatureElementViewset(viewsets.ModelViewSet):
    queryset = FeatureElement.objects.all()
    serializer_class = FeatureElementSerializer


class ProductFeatureViewset(viewsets.ModelViewSet):
    queryset = ProductFeature.objects.all()
    serializer_class = ProductFeatureSerializer
