from rest_framework import serializers

from .models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    status = serializers.ListField()
    class Meta:
        model = Address
        fields = '__all__'


class FirmCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmCategory
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class BankInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankInformation
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class DeliveryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCategory
        fields = '__all__'


class DeliveryTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryTime
        fields = '__all__'


class GetBankInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankInformation
        fields = ('id', 'name', 'firm_category')


class GetCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'region')


class GetCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class GetFirmCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FirmCategory
        fields = ('id', 'name')


class GetRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name', 'country')