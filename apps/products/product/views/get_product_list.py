from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from products.product.serializers.get_product_list import GetProductListSerializer


@api_view(['GET'])
def get_product_list(request):
	products = Product.objects.all()
	serializer = GetProductListSerializer(products, many=True)
	return Response(serializer.data, status=HTTP_200_OK)