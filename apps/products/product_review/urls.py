from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('product-question', ProductQuestionViewset, basename='ProductQuestionViewset')
router.register('review', ReviewViewset, basename='ReviewViewset')
router.register('media-review', MediaReviewViewset, basename='MediaReviewViewset')
