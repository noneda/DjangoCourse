"""
Database Models for User.
"""

from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for User."""

    def create_user(self, email, password=None, **extra_field):
        """Create Save and Return User"""
        if not email:
            raise ValueError(gettext_lazy("The Email must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save()

        return user

    # TODO: This feature is required when creating an administrator model from the user
    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a new superuser"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """User in the System"""

    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=255, default=None)

    # * No need, Django does it automatically.
    # ! password = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
