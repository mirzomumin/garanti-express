from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from products.product.models import Product


@api_view(['DELETE'])
def delete_product(request, product_id):
	product = get_object_or_404(Product, id=product_id)
	if product is not None:
		product.delete()
		return Response('Successfully deleted!', status=HTTP_200_OK)
	return Response('Product is already deleted or not found!',
		status=HTTP_400_BAD_REQUEST)