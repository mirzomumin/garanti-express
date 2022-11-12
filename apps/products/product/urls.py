from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('product', ProductViewset, basename='ProductViewset')
router.register('color', ColorViewset, basename='ColorViewset')
router.register('product-stock', ProductStockViewset, basename='ProductStockViewset')
router.register('media', MediaViewset, basename='MediaViewset')
