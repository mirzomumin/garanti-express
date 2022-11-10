from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
    def create_user(self, first_name, last_name, phone_number, email, role, password=None, is_admin=False, is_staff=False, is_active=True, balnace_id=None):
        if not first_name:
            raise ValueError("User must have a first_name")
        if not last_name:
            raise ValueError("User must have a last_name")
        if not phone_number:
            raise ValueError("User must have an phone number")
        if not email:
            raise ValueError("User must have a email")
        if not role:
            raise ValueError("User must have a role")
        # if not password:
        #     raise ValueError("User must have a password")
        # if not full_name:
        #     raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.balance_id = phone_number[-9:]
        user.email = email
        user.role = role
        user.set_password(password)  # change password to hash
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self, phone_number, email, gender, password=None):
        user = self.create_user(
            phone_number,
            email,
            is_staff=True,
        )
        user.set_password(password)
        return user

    def create_superuser(self, email, password, balance_id=None, **extra_fields):
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.superuser = True
        user.save(using=self._db)
        return user