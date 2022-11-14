from django.urls import path

from products.product.views.create_product import create_product
from products.product.views.get_product_detail import get_product_detail
from products.product.views.get_product_list import get_product_list
from products.product.views.delete_product import delete_product
from products.product.views.update_product import update_product


urlpatterns = [
	path('', get_product_list, name='products'),
	path('<int:product_id>/', get_product_detail, name='product'),
	path('create/', create_product, name='create_product'),
	path('<int:product_id>/update/', update_product, name='update_product'),
	path('<int:product_id>/delete/', delete_product, name='delete_product'),
]