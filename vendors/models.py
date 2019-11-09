from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(
        User, blank=True, related_name='employer'
    )

    def __str__(self):
        return self.name


class VendorItem(models.Model):
    name = models.CharField(max_length=100)
    available_on = models.DateTimeField()
    vendor = models.ForeignKey(
        'vendors.Vendor',
        related_name='items_for_sale',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
