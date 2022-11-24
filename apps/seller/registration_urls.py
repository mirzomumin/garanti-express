from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .registration import *

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('verify/', VerifyOTP.as_view()),
    path('sentotp/', VerifyEmailAPI.as_view()),
    path('resetpassword/', SetNewPasswordAPI.as_view()),
    path('login/', LoginAPI.as_view()),

]