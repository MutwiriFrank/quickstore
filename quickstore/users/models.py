from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

import random


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_("You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class Tenant(models.Model):
    tenant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    subdomain = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "tenant"


class Users(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(_("email address"), unique=True, null=False, blank=False)
    user_name = models.CharField(max_length=100)  # S
    tenant = models.ForeignKey(Tenant, models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    is_staff = models.BooleanField(default=False)  # people who can access admin
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    otp = models.CharField(max_length=6, null=True, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "user_name",
    ]

    class Meta:
        managed = True
        db_table = "Users"

    def __str__(self):
        return self.user_name

    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]  # Use of list comprehension
        code_items_for_otp = []

        for i in range(6):
            num = random.choice(number_list)
            code_items_for_otp.append(num)

        code_string = "".join(
            str(item) for item in code_items_for_otp
        )  # list comprehension again
        # A six digit random number from the list will be saved in top field
        self.otp = code_string
        super().save(*args, **kwargs)


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey(Tenant, models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Users, models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "customer"
