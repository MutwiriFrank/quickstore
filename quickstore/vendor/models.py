from django.db import models


class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey("users.Tenant", models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey("users.Users", models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    vendor_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = "vendor"

    def __str__(self):
        return self.vendor_name


class Vendoremployee(models.Model):
    vendor_employee_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey("users.Tenant", models.SET_NULL, blank=True, null=True)
    store = models.ForeignKey("vendor.Store", models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey("users.Users", models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "vendoremployee"

    def __str__(self):
        return self.user


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    tenant = models.ForeignKey("users.Tenant", models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey("geo.Location", models.SET_NULL, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    store_business_name = models.CharField(max_length=255, blank=True, null=True)
    store_phone_number = models.CharField(max_length=15, blank=True, null=True)
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "store"

    def __str__(self):
        return self.store_business_name


class Storetocustomer(models.Model):
    """
    These are unique customers per store
    """

    store_to_customer_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        "users.Customer", models.SET_NULL, blank=True, null=True
    )
    tenant = models.ForeignKey("users.Tenant", models.SET_NULL, blank=True, null=True)
    store = models.ForeignKey(Store, models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "storetocustomer"


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_full_name = models.CharField(max_length=255, blank=True, null=True)
    supplier_phone_number = models.CharField(max_length=15, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "supplier "

    def __str__(self):
        return self.supplier_full_name


class Supplierproducttostoreorder(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    store = models.ForeignKey(Store, models.SET_NULL, blank=True, null=True)
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    is_delivered = models.BooleanField(blank=True, null=True)
    is_paid = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "supplierproducttostoreorder"


class Supplierproducttostoreorderitem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        "products.Product", models.SET_NULL, blank=True, null=True
    )
    supplier_store = models.ForeignKey(
        "Supplierstore", models.SET_NULL, blank=True, null=True
    )
    order = models.ForeignKey(
        Supplierproducttostoreorder, models.SET_NULL, blank=True, null=True
    )
    quantity = models.IntegerField(blank=True, null=True)
    eff_start_date = models.DateField(blank=True, null=True)
    product_cost = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    product_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "supplierproducttostoreorderitem"


class Supplierstore(models.Model):
    supplier_store_id = models.AutoField(primary_key=True)
    supplier_business_name = models.CharField(max_length=255, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey("geo.Location", models.SET_NULL, blank=True, null=True)
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "supplierstore"


class Supplierstoretoproduct(models.Model):
    product = models.ForeignKey(
        "products.Product", models.SET_NULL, blank=True, null=True
    )
    supplier_store = models.ForeignKey(
        Supplierstore, models.SET_NULL, blank=True, null=True
    )
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(
        "products.Category", models.SET_NULL, blank=True, null=True
    )
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "supplierstoretoproduct"
