from django.db import models


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    location_from = models.CharField(max_length=255, blank=True, null=True)
    location_to = models.CharField(max_length=255, blank=True, null=True)
    delivery_fee = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    payment = models.ForeignKey(
        "payments.Payment", models.SET_NULL, blank=True, null=True
    )
    is_complete = models.BooleanField(blank=True, null=True)
    cleared_by = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "delivery"


class Orderitem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey("vendor.Store", models.SET_NULL, blank=True, null=True)
    store_to_product = models.ForeignKey(
        "vendor.Storetoproduct", models.SET_NULL, blank=True, null=True
    )
    order = models.ForeignKey("Orders", models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "orderitem"


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    payment = models.ForeignKey(
        "payments.Payment", models.SET_NULL, blank=True, null=True
    )
    delivery = models.ForeignKey(Delivery, models.SET_NULL, blank=True, null=True)
    order_time = models.DateTimeField(blank=True, null=True)
    delivery_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    customer = models.ForeignKey(
        "users.Customer", models.SET_NULL, blank=True, null=True
    )
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    is_paid = models.BooleanField(blank=True, null=True)
    is_delivered = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "orders"


class Wishlist(models.Model):
    wish_list_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        "users.Customer", models.CASCADE, blank=True, null=True
    )
    store_to_product = models.ForeignKey(
        "vendor.Storetoproduct", models.SET_NULL, blank=True, null=True
    )
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:

        db_table = "wishlist"
