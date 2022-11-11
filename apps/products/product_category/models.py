from django.db import models

from helpers.models import BaseModel
from multiselectfield import MultiSelectField

# Create your models here.

class Department(BaseModel):
	title = models.CharField(max_length=256)

	def __str__(self):
		return self.title


class Category(BaseModel):
	GENDER = (
		('male', 'male'),
		('female', 'female'),
		('unisex', 'unisex'),
		('kids', 'kids')
	)
	title = models.CharField(max_length=256)
	image = models.ImageField(upload_to='categories/', null=True, blank=True)
	is_delete = models.BooleanField(default=False)
	gender = MultiSelectField(choices=GENDER, max_length=100,
		max_choices=4)

	# Relations
	parent = models.ForeignKey('self', on_delete=models.CASCADE,
		related_name='subcategories', blank=True, null=True)
	department = models.ForeignKey(Department,
		on_delete=models.CASCADE, related_name='categories')

	def __str__(self):
		return self.title


class Brand(BaseModel):
	title = models.CharField(max_length=256)
	logo = models.ImageField(upload_to='brands/')
	is_delete = models.BooleanField(default=False)

	def __str__(self):
		return self.title