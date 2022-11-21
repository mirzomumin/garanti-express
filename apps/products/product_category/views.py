from django.shortcuts import render
from rest_framework import viewsets

from products.product_category.models import Department, Category, Brand
from products.product_category.serializers import DepartmentSerializer, CategorySerializer, BrandSerializer


# Create your views here.
class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewset(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
