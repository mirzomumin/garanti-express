from rest_framework import serializers

from products.product.models import (
	Product,
	Color,
	ProductStock,
	Media,
	Coupon,
	Collection)


class GetMediaListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Media
		fields = ('image',)


class GetProductStockListSerializer(serializers.ModelSerializer):
	media = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = ProductStock
		fields = ('media',)


	def get_media(self, obj):
		if obj.medias:
			media = obj.medias[0].image
			serializer = GetMediaListSerializer(media)
			return serializer.data


class GetProductListSerializer(serializers.ModelSerializer):
	product_stock = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Product
		fields = ('id', 'title', 'description', 'product_stock')

	def get_product_stock(self, obj):
		if obj.product_stocks:
			product_stock = obj.product_stocks[0].media
			serializer = GetProductStockListSerializer(product_stock)
			return serializer.data