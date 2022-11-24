from rest_framework import serializers

from products.product.models import (
	Product,
	Color,
	ProductStock,
	Media,
	Coupon,
	Collection)


class UpdateMediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Media
		exclude = ('id',)


class UpdateProductStockSerializer(serializers.ModelSerializer):
	medias = UpdateMediaSerializer(many=True)
	class Meta:
		model = ProductStock
		exclude = ('id',)


class UpdateProductSerializer(serializers.ModelSerializer):
	product_stocks = UpdateProductStockSerializer(many=True)
	class Meta:
		model = Product
		exclude = ('id',)