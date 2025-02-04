from django.db import models


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "brand"


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "category"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey(Brand, models.SET_NULL, blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "product"


class Variation(models.Model):
    variation_id = models.AutoField(primary_key=True)
    variation = models.CharField(max_length=50, blank=True, null=True)
    product = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "variation"
