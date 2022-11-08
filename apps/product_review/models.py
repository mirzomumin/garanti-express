from django.db import models

from helpers.models import BaseModel
from product.models import ProductStock
# Create your models here.


class ProductQuestion(BaseModel):
	product_stock = models.ForeignKey(ProductStock,
		on_delete=models.CASCADE, related_name='product_questions')
	# user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
	# 	related_name='product_questions')
	question = models.CharField(max_length=256)
	answer = models.CharField(max_length=256, null=True, blank=True)
	is_answered = models.BooleanField(default=False)
	answered_at = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return f'Question {self.question} for\
		product {self.product_stock}'


class Review(BaseModel):
	product_stock = models.ForeignKey(ProductStock,
		on_delete=models.CASCADE, related_name='reviews')
	# user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
	# 	related_name='reviews')
	comment = models.TextField()
	rate = models.PositiveSmallIntegerField(blank=True, null=True)


class MediaReview(BaseModel):
	review = models.ForeignKey(Review, on_delete=models.CASCADE,
		related_name='media_reviews')
	image = models.ImageField(upload_to='media-reviews/images/')
	video = models.FileField(upload_to='media-reviews/video/')
	is_image = models.BooleanField(default=True)