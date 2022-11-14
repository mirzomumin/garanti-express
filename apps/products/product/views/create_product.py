from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
import json

from products.product.serializers.create_product import (
	CreateProductSerializer,
	CreateProductStockSerializer,
	CreateMediaSerializer
)


@api_view(['POST'])
def create_product(request):
	product_serializer = CreateProductSerializer(
		data=request.data,
		context={'request': request})
	if product_serializer.is_valid(raise_exception=True):
		product_serializer.save(seller=request.user.seller)
		product_stocks = request.data['product']['product_stocks']
		for product_stock in product_stocks:
			product_stock = json.loads(product_stock)
			product_stock['product'] = product_serializer.data.get('id')
			product_stock_serializer = CreateProductStockSerializer(data=product_stock)
			if product_stock_serializer.is_valid(raise_exception=True):
				product_stock_serializer.save()
				medias = product_stock['medias']
				for media in medias:
					media = json.loads(media)
					media.product_stock = product_serializer.data.get('id')
					media_serializer = CreateMediaSerializer(media)
					media_serializer.save()
		return Response(product_serializer.data, status=HTTP_201_CREATED)
	return Response({'response': 'Bad Request!'}, status=HTTP_400_BAD_REQUEST)


