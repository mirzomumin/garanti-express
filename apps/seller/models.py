from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

from helpers.models import BaseModel
from user.models import CustomUser
from products.product_category.models import Category

from products.product_category.models import Department


# Create your models here.

class Contact(BaseModel):
    STATUS = (
        ('financier', 'financier'),
        ('manager', 'manager'),
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = PhoneNumberField()
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.name


class Address(BaseModel):
    STATUS = (
        ('billing', 'billing'),
        ('firm', 'firm'),
        ('shipping', 'shipping'),
        ('return_shipping', 'return_shipping')
    )
    province = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip_code = models.PositiveIntegerField()
    status = MultiSelectField(choices=STATUS, max_length=64,
                              max_choices=4)

    def __str__(self):
        return f'{self.province} {self.district}\
		{self.address}'


class FirmCategory(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Country(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Region(BaseModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE,
        related_name='regions')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE,
        related_name='cities')
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class BankInformation(BaseModel):
    firm_category = models.ForeignKey(FirmCategory,
                                      on_delete=models.CASCADE, related_name='bank_informations')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Seller(BaseModel):
    website_url = models.URLField(null=True, blank=True)
    referal_code = models.CharField(max_length=255, null=True, blank=True)
    bank_information_number = models.PositiveIntegerField()
    # logo = models.ImageField(upload_to='logo/', null=True, blank=True)

    # Relations
    user = models.OneToOneField(CustomUser,
                                on_delete=models.CASCADE, related_name='seller')
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name='sellers')
    addresses = models.ManyToManyField(Address, blank=True,
                                       related_name='sellers')
    finance_contact = models.ForeignKey(Contact,
                                        on_delete=models.CASCADE, related_name='finance_sellers')
    manager_contact = models.ForeignKey(Contact,
                                        on_delete=models.CASCADE, related_name='manager_sellers')
    region = models.ForeignKey(Region, on_delete=models.CASCADE,
                               related_name='sellers')
    city = models.ForeignKey(City, on_delete=models.CASCADE,
                             related_name='sellers')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                         related_name='sellers')
    firm_category = models.ForeignKey(FirmCategory, on_delete=models.CASCADE,
                                      related_name='sellers')
    bank_information = models.ForeignKey(BankInformation,
                                         on_delete=models.CASCADE, related_name='sellers')


class DeliveryCategory(BaseModel):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               related_name='delivery_categories')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DeliveryTime(BaseModel):
    delivery_category = models.ForeignKey(DeliveryCategory,
                                          on_delete=models.CASCADE, related_name='delivery_times')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
