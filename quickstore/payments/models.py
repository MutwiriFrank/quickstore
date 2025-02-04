from django.db import models


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_channel = models.CharField(max_length=50, blank=True, null=True)
    payment_amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    country = models.ForeignKey("geo.Country", models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "payment"
