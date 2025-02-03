from django.db import models

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

import random

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email,  user_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))
   

        email = self.normalize_email(email) 
        user = self.model(email=email, user_name=user_name,  **other_fields)
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
        
class Country (models.Model):
    country_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    country_code = models.CharField(unique=True, max_length=10)
    country_name = models.CharField(max_length=100)

    class Meta:
        db_table = "country"
    
class Users( AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'), unique=True, null=False, blank=False)
    user_name = models.CharField(max_length=100 ) # S
    tenant = models.ForeignKey(Tenant, models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    is_staff = models.BooleanField(default=False) # people who can access admin
    is_active = models.BooleanField(default=True    )
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    otp = models.CharField(max_length=6, null=True, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name',]
    
    class Meta:
        managed = True
        db_table = 'Users'

    def __str__(self):
        return self.user_name

    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]  # Use of list comprehension
        code_items_for_otp = []

        for i in range(6):
            num = random.choice(number_list)
            code_items_for_otp.append(num)

        code_string = "".join(str(item)
        for item in code_items_for_otp)  # list comprehension again
        # A six digit random number from the list will be saved in top field
        self.otp = code_string
        super().save(*args, **kwargs)

    class Meta:
        db_table = "users"



class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "brand"


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "category"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey(Tenant, models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Users, models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "customer"


class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey(Tenant, models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Users, models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    vendor_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = "vendor"


class Vendoremployee(models.Model):
    vendor_employee_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey(Tenant, models.SET_NULL, blank=True, null=True)
    store = models.ForeignKey('Store', models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Users, models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "vendoremployee"


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    location_from = models.CharField(max_length=255, blank=True, null=True)
    location_to = models.CharField(max_length=255, blank=True, null=True)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment = models.ForeignKey('Payment', models.SET_NULL, blank=True, null=True)
    is_complete = models.BooleanField(blank=True, null=True)
    cleared_by = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "delivery"


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    location_name = models.CharField(max_length=255, blank=True, null=True)
    street_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "location"


class Orderitem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey('Store', models.SET_NULL, blank=True, null=True)
    store_to_product = models.ForeignKey('Storetoproduct', models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey('Orders', models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "orderitem"


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    payment = models.ForeignKey('Payment', models.SET_NULL, blank=True, null=True)
    delivery = models.ForeignKey(Delivery , models.SET_NULL, blank=True, null=True)
    order_time = models.DateTimeField(blank=True, null=True)
    delivery_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    customer= models.ForeignKey(Customer, models.SET_NULL, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_paid = models.BooleanField(blank=True, null=True)
    is_delivered = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "orders"


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_channel = models.CharField(max_length=50, blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "payment"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey(Brand, models.SET_NULL, blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "product"


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey(Tenant, models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey(Location, models.SET_NULL, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    store_business_name = models.CharField(max_length=255, blank=True, null=True)
    store_phone_number = models.CharField(max_length=15, blank=True, null=True)
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "store"


class Storecategory(models.Model):
    store_category_id = models.AutoField(primary_key=True)
    store_category_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "storecategory"


class Storetocustomer(models.Model):  
    '''
    These are unique customers per store
    '''
    store_to_customer_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.SET_NULL, blank=True, null=True) 
    tenant = models.ForeignKey(Tenant, models.SET_NULL, blank=True, null=True)
    store = models.ForeignKey(Store, models.SET_NULL  , blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "storetocustomer"


class Storetoproduct(models.Model):
    store_to_product_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
    store = models.ForeignKey(Store, models.SET_NULL   , blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)
    store_category = models.ForeignKey(Storecategory, models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "storetoproduct"


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_full_names = models.CharField(max_length=255, blank=True, null=True)
    supplier_phone_number = models.CharField(max_length=15, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "supplier "


class Supplierproducttostoreorder(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    store = models.ForeignKey(Store, models.SET_NULL, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_delivered = models.BooleanField(blank=True, null=True)
    is_paid = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "supplierproducttostoreorder"


class Supplierproducttostoreorderitem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
    supplier_store = models.ForeignKey('Supplierstore', models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Supplierproducttostoreorder, models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    eff_start_date = models.DateField(blank=True, null=True)
    product_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True) 
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "supplierproducttostoreorderitem"


class Supplierstore(models.Model):
    supplier_store_id = models.AutoField(primary_key=True)
    supplier_business_name = models.CharField(max_length=255, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey(Location, models.SET_NULL, blank=True, null=True)
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'supplierstore'


class Supplierstoretoproduct(models.Model):
    product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
    supplier_store = models.ForeignKey(Supplierstore, models.SET_NULL, blank=True, null=True)
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'supplierstoretoproduct'


class Variation(models.Model):
    variation_id = models.AutoField(primary_key=True)
    variation = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'variation'


class Wishlist(models.Model):
    wish_list_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.CASCADE, blank=True, null=True)
    store_to_product = models.ForeignKey(Storetoproduct, models.SET_NULL, blank=True, null=True)
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'wishlist'