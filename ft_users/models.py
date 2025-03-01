from collections.abc import Collection
from typing import Any
from django.db import models
from datetime import datetime

from ft_api.choices import Suffix, Gender, CivilStatus

from django.contrib.auth.models import AbstractUser, UserManager, Group

class Manager(UserManager):
    def create_user(self, username: str, email: str | None = None, password: str | None = None, **extra_fields: Any) -> Any:
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class CustomerUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, unique=True)

    image = models.ImageField(max_length=255, unique=True)

    # General Information
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    suffix = models.CharField(
        max_length=255,
        choices = Suffix,
        default = '',
        blank=True,
        null=True
    )
    gender = models.CharField(
        max_length=255, 
        choices=Gender, 
        default='', 
        blank=True, 
        null=True
        )

    # More Information
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    civil_status = models.CharField(
        max_length=255,
        choices = CivilStatus,
        default = 'Single',
        blank=True,
        null=True
        )
    emergency_contact = models.CharField(max_length=255)
    emergency_contact_number = models.CharField(max_length=255)


    # Contact Information
    phone_number = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)

    # Account Information
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password']

    objects = Manager()

    def __str__(self):
        return f'{self.full_name}'
    
    def has_module_perms(self, app_label: str) -> bool:
        return self.is_superuser

    def has_perms(self, perm_list: Collection[str]) -> bool:
        return self.is_superuser
    
    @property
    def full_name(self):
        if self.first_name and self.last_name:
            if self.suffix:
                return f'{self.last_name}, {self.suffix}, {self.first_name} {self.middle_name}'.title()
            return f'{self.last_name}, {self.first_name} {self.middle_name}'.title()
        return f'{self.first_name} {self.middle_name}'.title()