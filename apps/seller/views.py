import json

from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from seller.models import Seller, FirmCategory, Country, Region, City, BankInformation
from .serializers import *
from user.models import CustomUser


class SellerViewset(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    @action(methods=['post'], detail=False)
    def post(self, request):
        data = request.data
        # data = json.loads(data_re)
        address = data["addresses"]
        finance_contact = data["finance_contact"]
        manager_contact = data["manager_contact"]
        # print(address)
        address_serializer = AddressSerializer(data=address, many=True)
        finance_contact_serializer = ContactSerializer(data=finance_contact)
        manager_contact_serializer = ContactSerializer(data=manager_contact)
        if not address_serializer.is_valid():
            return Response(address_serializer.errors, status=HTTP_400_BAD_REQUEST)
        if not finance_contact_serializer.is_valid():
            return Response(finance_contact_serializer.errors, status=HTTP_400_BAD_REQUEST)
        if not manager_contact_serializer.is_valid():
            return Response(manager_contact_serializer.errors, status=HTTP_400_BAD_REQUEST)

        email = data['email']
        user = CustomUser.objects.filter(email=email)
        if user.exists():
            us = user.last()
            us.legal_name = data['legal_name']
            us.brand_name = data['brand_name']
            us.phone = data['phone_number']
            us.set_password(data['password'])
            us.save()
        else:
            return Response({"error": "User doesn't exists"}, status=HTTP_400_BAD_REQUEST)

        # Create Instances

        address_serializer.save()
        finance_contact_serializer.save()
        manager_contact_serializer.save()

        # Get id from Instances

        address_instances = [i.get('id') for i in address_serializer.data]
        finance_contact_instance = finance_contact_serializer.data.get('id')
        manager_contact_instance = manager_contact_serializer.data.get('id')

        # Create full seller object
        token, created = Token.objects.get_or_create(user=user.last())
        data['user'] = user.last().id
        data['token'] = token.key,
        data['addresses'] = address_instances
        data['finance_contact'] = finance_contact_instance
        data['manager_contact'] = manager_contact_instance
        seller_instance = SellerSerializer(data=data)
        if seller_instance.is_valid():
            seller_instance.save()

            return Response(seller_instance.data, status=HTTP_201_CREATED)
        return Response(seller_instance.errors, status=HTTP_400_BAD_REQUEST)


class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AddressViewset(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class FirmCategoryViewset(viewsets.ModelViewSet):
    queryset = FirmCategory.objects.all()
    serializer_class = FirmCategorySerializer


class CountryViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(methods=['post'], detail=False)
    def post(self, request):
        data = request.data.get('data')
        regions = 0
        city = 0
        for i in data:
            region_name = i.get('il_adi')
            region = Region.objects.create(
                name=region_name,
                country_id=3
            )
            regions += 1
            print(region_name, '--------------')
            for n in i.get('ilceler'):
                city_name = n.get('ilce_adi')
                print(city_name)
                city = City.objects.create(
                    region=region,
                    name=city_name
                )
        return Response("Created")


class RegionViewset(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    country_id = openapi.Parameter('country_id', openapi.IN_QUERY,
        description="country_id manual param", type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(method='get', manual_parameters=[country_id])
    @action(methods=['get'], detail=False)
    def country_regions(self, request):
        country_id = request.query_params.get("country_id")
        regioins = Region.objects.filter(
            country__id=country_id
        ).all()
        serializer = GetRegionSerializer(regioins, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class CityViewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    region_id = openapi.Parameter('region_id', openapi.IN_QUERY,
        description="region_id manual param", type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(method='get', manual_parameters=[region_id])
    @action(methods=['get'], detail=False)
    def region_cities(self, request):
        region_id = request.query_params.get("region_id")
        cities = City.objects.filter(
            region__id=region_id
        ).values('id', 'name', 'region')
        serializer = GetCitySerializer(cities, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class BankInformationViewset(viewsets.ModelViewSet):
    queryset = BankInformation.objects.all()
    serializer_class = BankInformationSerializer
    firm_category_id = openapi.Parameter('firm_category_id', openapi.IN_QUERY,
        description="firm_category_id manual param", type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(method='get', manual_parameters=[firm_category_id])
    @action(methods=['get'], detail=False)
    def category_info(self, request):
        firm_category_id = request.query_params.get("firm_category_id")
        bank_informations = BankInformation.objects.filter(
            firm_category__id=firm_category_id
        ).all()
        serializer = GetBankInformationSerializer(bank_informations, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class DeliveryCategoryViewset(viewsets.ModelViewSet):
    queryset = DeliveryCategory.objects.all()
    serializer_class = DeliveryCategorySerializer


class DeliveryTimeViewset(viewsets.ModelViewSet):
    queryset = DeliveryTime.objects.all()
    serializer_class = DeliveryTimeSerializer
