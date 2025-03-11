from django.db import models


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "brand"

    def __str__(self):
        return self.brand_name


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.category_name


class Product(models.Model):
    IS_DIGITAL_CHOICES = [("True", "True"), ("False", "False")]
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey(Brand, models.SET_NULL, blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    image_url = models.TextField
    is_digital = models.CharField(
        max_length=5, null=True, blank=True, choices=IS_DIGITAL_CHOICES, default="False"
    )
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.product_name


class Variation(models.Model):
    variation_id = models.AutoField(primary_key=True)
    variation = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "variation"

    def __str__(self):
        return self.variation


class Storecategory(models.Model):
    store_category_id = models.AutoField(primary_key=True)
    store_category_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "storecategory"

    def __str__(self):
        return self.store_category_name


class Storetoproduct(models.Model):
    store_to_product_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
    store = models.ForeignKey("vendor.Store", models.SET_NULL, blank=True, null=True)
    product_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    quantity = models.DecimalField(
        default=100, null=True, blank=True, max_digits=11, decimal_places=2
    )
    eff_start_date = models.DateField(blank=True, null=True)
    eff_end_date = models.DateField(blank=True, null=True)
    store_category = models.ForeignKey(
        Storecategory, models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "storetoproduct"
