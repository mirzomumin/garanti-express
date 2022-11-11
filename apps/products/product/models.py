from django.db import models

from helpers.models import BaseModel
<<<<<<< HEAD:apps/product/models.py
from product_category.models import Department, Category, Brand
from seller.models import Seller
=======
from products.product_category.models import Department, Category, Brand
>>>>>>> diyorbek:apps/products/product/models.py

# Create your models here.

class Product(BaseModel):
	STATUS = (
		('pending', 'Pending'),
		('approved', 'Approved'),
		('canceled', 'Canceled'),
		('deleted', 'Deleted')
	)
	GENDER = (
		('male', 'Male'),
		('female', 'Female'),
		('unisex', 'Unisex'),
		('kids', 'Kids')
	)
	title = models.CharField(max_length=256)
	description = models.TextField()
	model = models.CharField(max_length=256)
	barcode = models.PositiveIntegerField(unique=True)
	manufacturer = models.CharField(max_length=256)
	status = models.CharField(max_length=10, choices=STATUS)
	published_at = models.DateTimeField(blank=True, null=True)
	gender = models.CharField(max_length=10, choices=GENDER)

	# Relations
	category = models.ForeignKey(Category,
		on_delete=models.CASCADE, related_name='products')
	brand = models.ForeignKey(Brand,
		on_delete=models.CASCADE, related_name='products')
	seller = models.ForeignKey(Seller,
		on_delete=models.CASCADE, related_name='products')


	def __str__(self):
		return self.title


class Color(BaseModel):
	title = models.CharField(max_length=256)
	code = models.PositiveIntegerField(unique=True)
	is_delete = models.BooleanField(default=False)

	def __str__(self):
		return self.title


class ProductStock(BaseModel):
	good_kdv = models.PositiveIntegerField()
	stock_code = models.PositiveIntegerField(unique=True)
	amount = models.PositiveIntegerField()
	is_discount = models.BooleanField(default=False)
	market_price = models.PositiveIntegerField()
	gr_price = models.PositiveIntegerField()
	discount = models.PositiveIntegerField()
	comission = models.PositiveIntegerField()
	weight = models.PositiveIntegerField()

	# Relations
	product = models.ForeignKey(Product, on_delete=models.CASCADE,
		related_name='product_stocks')
	color = models.ForeignKey(Color, on_delete=models.CASCADE,
		related_name='product_stocks')


class Media(BaseModel):
	product_stock = models.ForeignKey(ProductStock,
		on_delete=models.CASCADE, related_name='medias')
	image = models.ImageField(upload_to='products/images/')
	video = models.FileField(upload_to='products/videos/')
	is_image = models.BooleanField(default=True)


class Coupon(BaseModel):
	STATUS = (
		('seller', 'seller'),
		('category', 'category'),
		('product', 'product'),
		('general', 'general'),
		('brand', 'brand')
	)
	limit_amount = models.PositiveIntegerField()
	limit_quantity = models.PositiveIntegerField()
	status = models.CharField(max_length=20, choices=STATUS)

	# Relations
	seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
		related_name='coupons')
	category = models.ManyToManyField(Category,
		related_name='coupons')
	product = models.ManyToManyField(Product,
		related_name='coupons')
	brand = models.ManyToManyField(Brand,
		related_name='coupons')


class Collection(BaseModel):
	STATUS = (
		('seller', 'seller'),
		('category', 'category'),
		('product', 'product'),
		('general', 'general'),
		('brand', 'brand')
	)
	name = models.CharField(max_length=255)
	image = models.ImageField(upload_to='products/collections/')
	status = models.CharField(max_length=20, choices=STATUS)

	# Relations
	seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
		related_name='collections')
	category = models.ManyToManyField(Category,
		related_name='collections')
	product = models.ManyToManyField(Product,
		related_name='collections')
	brand = models.ManyToManyField(Brand,
		related_name='collections')

	def __str__(self):
		return self.name