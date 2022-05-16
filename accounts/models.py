import email

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
    # Create standard user
    def create_user(self, email, full_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('User must have an email address')
        if not full_name:
            raise ValueError('User must provide a full name')
        if not password:
            raise ValueError('User must provide a password')
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name = full_name
        )
        user_obj.set_password(password) # Defined user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.set_password(password) # Defined user password
        user_obj.save(using=self._db) # Defined user password
        return user_obj

    # Create a staff user
    def create_staff_user(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True
        )
        return user

    # Create superuser
    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)  # If active can login
    staff = models.BooleanField(default=False)  # If the user is a staff member
    admin = models.BooleanField(default=False)  # If the user has superuser permissions
    timestamp = models.DateTimeField(auto_now_add=True) # Get the time that the user has been created
    #confirm = models.BooleanField(defaul=False) # Confirmed email
    #confirmed_date = models.DateTimeField(auto_now_add=True) # Get the time that the email has been confirmed

    USERNAME_FIELD = 'email'    # That is now the username
    REQUIRED_FIELDS = ['full_name']    # Email, name and password are required

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self): # Return the name of the user
        return self.full_name

    # def get_short_name(self):
    #     return self.email

    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

    # Check if is staff
    @property
    def is_staff(self):
        return self.staff

    # Check if is admin
    @property
    def is_admin(self):
        return self.admin

    # Check if is active
    @property
    def is_active(self):
        return self.active

