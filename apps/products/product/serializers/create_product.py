from rest_framework import serializers

from products.product.models import (
	Product,
	Color,
	ProductStock,
	Media,
	Coupon,
	Collection)


class CreateMediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Media
		fields = '__all__'


class CreateProductStockSerializer(serializers.ModelSerializer):
	medias = CreateMediaSerializer(many=True)
	class Meta:
		model = ProductStock
		fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):
	product_stocks = CreateProductStockSerializer(many=True)
	class Meta:
		model = Product
		fields = '__all__'