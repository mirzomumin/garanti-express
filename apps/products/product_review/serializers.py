from rest_framework import serializers

from .models import *


class ProductQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuestion
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MediaReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaReview
        fields = '__all__'
