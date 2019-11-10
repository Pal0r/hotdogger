from datetime import timedelta

from django.utils.timezone import now

from vendors.models import Vendor, VendorItem


def create_hotdogs(count):
    vendor_1 = Vendor.objects.first()
    vendor_2 = Vendor.objects.last()
    hotdogs = []
    next_month = now() + timedelta(days=30)

    for i in range(count):
        hotdogs.append(
            VendorItem(
                name=f"bulk dog {i}",
                vendor=vendor_1 if i % 2 == 0 else vendor_2,
                available_on=now() if i % 3 == 0 else next_month
            )
        )

    VendorItem.objects.bulk_create(hotdogs)


def delete_bulk_items():
    VendorItem.objects.filter(name__icontains="bulk").delete()