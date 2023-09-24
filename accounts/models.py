from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import UserAccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)
    username = models.CharField(_("username"), max_length=100, unique=True)
    email = models.CharField(_("email"), max_length=150, unique=True)
    phone_number = models.CharField(_("phone number"), max_length=50)

    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    last_login = models.DateTimeField(_("last login"), auto_now_add=True)
    is_admin = models.BooleanField(_("is admin ?"), default=False)
    is_staff = models.BooleanField(_("is staff ?"), default=False)
    is_active = models.BooleanField(_("is active ?"), default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
