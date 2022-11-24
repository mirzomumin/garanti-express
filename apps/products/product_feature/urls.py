from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('feature', FeatureViewset, basename='FeatureViewset')
router.register('feature-element', FeatureElementViewset, basename='FeatureElementViewset')
router.register('product-feature', ProductFeatureViewset, basename='ProductFeatureViewset')
