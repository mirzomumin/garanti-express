from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('department', DepartmentViewset, basename='DepartmentViewset')
router.register('category', CategoryViewset, basename='CategoryViewset')
router.register('brand', BrandViewset, basename='BrandViewset')
