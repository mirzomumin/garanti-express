from django.contrib import admin

from products.product_category.models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(Brand)