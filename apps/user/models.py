from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField

from .manager import CustomUserManager


# Create your models here.

class CustomUser(AbstractBaseUser):
    STATUS = (
        ('seller', 'seller'),
        ('customer', 'customer'),
    )
    legal_name = models.CharField(max_length=255, null=True, blank=True)
    brand_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField()
    status = models.CharField(max_length=10, choices=STATUS, default="seller")

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # <- admin user, not super user
    superuser = models.BooleanField(default=False)  # <- super user
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=200, null=True, blank=True)

    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS = ['phone']  # <- email and password are required by default

    class Meta:
        app_label = "user"
        db_table = "user"

    def __str__(self):
        return f'{self.email}'

    def has_perm(self, perm, obj=None):
        """Does the user has a specific permission"""
        return True

    def has_module_perms(self, app_lable):
        """Does the user has permission to view a specific app"""
        return True

    @property
    def is_staff(self):
        """Is the user a staff member"""
        return self.staff

    @property
    def is_superuser(self):
        """Is the user a admin member"""
        return self.superuser

    @property
    def is_active(self):
        """Is the user active"""
        return self.active

    @property
    def is_admin(self):
        return self.admin

    # hook the user manager to objects
    objects = CustomUserManager()