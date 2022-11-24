from rest_framework import serializers

from .models import *


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'


class FeatureElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureElement
        fields = '__all__'


class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = '__all__'
