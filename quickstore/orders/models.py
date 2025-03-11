from django.db import models
from django.conf import settings


class Delivery(models.Model):
    DELIVERY_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    delivery_id = models.AutoField(primary_key=True)
    location_from = models.CharField(max_length=255, blank=True, null=True)
    location_to = models.CharField(max_length=255, blank=True, null=True)
    delivery_fee = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    payment = models.ForeignKey(
        "payments.Payment", models.SET_NULL, blank=True, null=True
    )
    delivery_date = models.DateTimeField(null=False, blank=False)
    delivery_status = models.CharField(
        blank=True, null=True, choices=DELIVERY_STATUS_CHOICES
    )
    cleared_by = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(class)s_created_by",
    )
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(class)s_updated_by",
    )

    def __str__(self):
        return f"{self.location_to} + '-' + {self.delivery_date}"

    class Meta:
        db_table = "delivery"


class Orderitem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey("vendor.Store", models.SET_NULL, blank=True, null=True)
    store_to_product = models.ForeignKey(
        "products.Storetoproduct", models.SET_NULL, blank=True, null=True
    )
    order = models.ForeignKey("Orders", models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(class)s_created_by",
    )
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(class)s_updated_by",
    )

    def __str__(self):
        return f"{self.store_to_product} + '-' + {self.store_id}"

    class Meta:
        db_table = "orderitem"


class Orders(models.Model):
    ORDER_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
        ("Reversed", "Reversed"),
    ]

    order_id = models.AutoField(primary_key=True)
    payment = models.ForeignKey(
        "payments.Payment", models.SET_NULL, blank=True, null=True
    )
    delivery = models.ForeignKey(Delivery, models.SET_NULL, blank=True, null=True)
    order_time = models.DateTimeField(blank=True, null=True)
    delivery_time = models.DateTimeField(blank=True, null=True)
    customer = models.ForeignKey(
        "users.Customer", models.SET_NULL, blank=True, null=True
    )
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    is_paid = models.BooleanField(blank=True, null=True)
    order_status = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=ORDER_STATUS_CHOICES,
        default="Pending",
    )
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(class)s_created_by",
    )
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(class)s_updated_by",
    )

    def __str__(self):
        return f"{self.order_id} + '-' + {self.order_time}"

    class Meta:
        db_table = "orders"


class Wishlist(models.Model):
    wish_list_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        "users.Customer", models.CASCADE, blank=True, null=True
    )
    store_to_product = models.ForeignKey(
        "products.Storetoproduct", models.SET_NULL, blank=True, null=True
    )
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(class)s_created_by",
    )
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="%(class)s_updated_by",
    )

    def __str__(self):
        return f"{self.store_to_product} + '-' + {self.wish_list_id}"

    class Meta:

        db_table = "wishlist"
