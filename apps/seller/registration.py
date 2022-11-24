import email

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .registration_serializers import *
from .emails import *
from user.models import CustomUser


class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                otp = send_otp_via_email(serializer.data['email'])
                return Response({
                    'message': 'registration successfully check email',
                    'data': serializer.data,
                    'otp': otp,

                }, status=status.HTTP_201_CREATED)

            return Response({
                'message': 'something went wrong',
                'data': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                'error': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = ResetAccountSerializer(data=data)

            if serializer.is_valid():
                email = serializer.data['email']
                users = CustomUser.objects.filter(email=email)
                if not users:
                    return Response({
                        'status': 400,
                        'data': 'invalid email'
                    }, status=status.HTTP_400_BAD_REQUEST)
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'message': 'sent otp, check email',
                    'data': serializer.data,
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)

            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']

                users = CustomUser.objects.filter(email=email)
                if not users:
                    return Response({
                        'status': 400,
                        'data': 'invalid email'
                    }, status=status.HTTP_400_BAD_REQUEST)

                if users[0].otp != otp:
                    return Response({
                        'status': 400,
                        'data': 'wrong otp'
                    }, status=status.HTTP_400_BAD_REQUEST)
                if users[0].otp == otp:
                    users[0].is_verified = True
                    users[0].save()
                    return Response({
                        'message': 'account verified, go to reset password',
                        'data': {}
                    }, status=status.HTTP_200_OK)

            return Response({
                'message': 'something went wrong',
                'data': serializer.errors,
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        except Exception as e:
            return Response({
                'error': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)


class SetNewPasswordAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = SetNewPasswordSerializer(data=data)

            users = CustomUser.objects.get(email=email)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                password = serializer.data['password']
                if not users:
                    return Response({
                        'status': 400,
                        'data': 'invalid email'
                    }, status=status.HTTP_400_BAD_REQUEST)

                if users[0].otp != otp:
                    return Response({
                        'status': 400,
                        'data': 'wrong otp'
                    }, status=status.HTTP_400_BAD_REQUEST)
                if users[0].otp == otp:
                    users[0].is_verified = True
                    users[0].set_password(password)
                    users[0].save()
                    return Response({
                        'message': 'changed password successfully',
                        'data': {}
                    }, status=status.HTTP_200_OK)

            return Response({
                'message': 'something went wrong',
                'data': serializer.errors,
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        except Exception as e:
            return Response({
                'error': str(e),
            }, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        users = CustomUser.objects.filter(email=email)
        if users.exists():
            user = authenticate(request, email=email, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=users.last())
                text = {
                    "token": token.key,
                    "user": {
                        "id": users.last().id,
                        "legal_name": users.last().legal_name
                    }
                }
                return Response(text, status=200)

            return Response({"error": "Password is invalid"}, status=400)
        return Response({"error": "Email or password is invalid"}, status=400)
