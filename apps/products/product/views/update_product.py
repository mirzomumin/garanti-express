from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from products.product.models import Product
from products.product.serializers.update_product import (
	UpdateProductSerializer
)


@api_view(['PUT'])
def update_product(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	serializer = UpdateProductSerializer(product)
	if serializer.is_valid(raise_exception=True):
		serializer.save()
		return Response(serializer.data, status=HTTP_200_OK)
	return Response({'response': 'Bad Request!'},
		status=HTTP_400_BAD_REQUEST)