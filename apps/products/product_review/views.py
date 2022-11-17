from django.shortcuts import render
from rest_framework import viewsets

from apps.products.product_review.models import ProductQuestion, Review, MediaReview
from apps.products.product_review.serializers import ProductQuestionSerializer, ReviewSerializer, MediaReviewSerializer


# Create your views here.
class ProductQuestionViewset(viewsets.ModelViewSet):
    queryset = ProductQuestion.objects.all()
    serializer_class = ProductQuestionSerializer


class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class MediaReviewViewset(viewsets.ModelViewSet):
    queryset = MediaReview.objects.all()
    serializer_class = MediaReviewSerializer
