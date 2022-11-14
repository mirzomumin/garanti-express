from rest_framework import serializers

from products.product.models import (
	Product,
	Color,
	ProductStock,
	Media,
	Coupon,
	Collection)


class GetMediaDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Media
		fields = '__all__'


class GetProductStockDetailSerializer(serializers.ModelSerializer):
	medias = GetMediaDetailSerializer(many=True)
	class Meta:
		model = ProductStock
		fields = '__all__'


class GetProductDetailSerializer(serializers.ModelSerializer):
	product_stocks = GetProductStockDetailSerializer(many=True)
	class Meta:
		model = Product
		fields = '__all__'