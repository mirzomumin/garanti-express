from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('seller', SellerViewset, basename='SellerViewset')
router.register('contact', ContactViewset, basename='ContactViewset')
router.register('address', AddressViewset, basename='AddressViewset')
router.register('firm-category', FirmCategoryViewset, basename='FirmCategoryViewset')
router.register('country', CountryViewset, basename='CountryViewset')
router.register('region', RegionViewset, basename='RegionViewset')
router.register('city', CityViewset, basename='CityViewset')
router.register('bank-information', BankInformationViewset, basename='BankInformationViewset')
router.register('delivery-category', DeliveryCategoryViewset, basename='DeliveryCategoryViewset')
router.register('delivery-time', DeliveryTimeViewset, basename='DeliveryTimeViewset')
