from django.db import models


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    country_code = models.CharField(unique=True, max_length=10)
    country_name = models.CharField(max_length=100)

    class Meta:
        db_table = "country"


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


class City(models.Model):
    country = models.ForeignKey(Country, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=100)

    class Meta:
        db_table = "city"
