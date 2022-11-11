from django.contrib import admin

from seller.models import *

# Register your models here.
admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(FirmCategory)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(BankInformation)
admin.site.register(Seller)
admin.site.register(DeliveryCategory)
admin.site.register(DeliveryTime)