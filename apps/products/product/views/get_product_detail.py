from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


from products.product.models import Product
from products.product.serializers.get_product_detail import (
	# GetMediaDetailSerializer,
	# GetProductStockDetailSerializer,
	GetProductDetailSerializer
)


@api_view(['GET'])
def get_product_detail(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	serializer = GetProductDetailSerializer(product)
	return Response(serializer.data, status=HTTP_200_OK)