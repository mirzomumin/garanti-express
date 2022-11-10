from django.db import models

from helpers.models import BaseModel
from products.product.models import ProductStock
from products.product_category.models import Department
# Create your models here.


class Feature(BaseModel):
	title = models.CharField(max_length=256)

	# Relations
	department = models.ForeignKey(Department,
		on_delete=models.CASCADE, related_name='features')

	def __str__(self):
		return self.title


class FeatureElement(BaseModel):
	title = models.CharField(max_length=256)

	# Relations
	feature = models.ForeignKey(Feature,
		on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class ProductFeature(BaseModel):

	# Relations
	product_stock = models.ForeignKey(ProductStock,
		on_delete=models.CASCADE, related_name='product_features')
	feature = models.ForeignKey(Feature, on_delete=models.CASCADE,
		related_name='product_features')
	feature_elements = models.ManyToManyField(FeatureElement,
		related_name='product_features')