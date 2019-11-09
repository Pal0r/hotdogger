import factory
from django.utils.timezone import now

from vendors.models import VendorItem, Vendor


class VendorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vendor

    name = factory.Sequence(lambda n: f"Vendor-{n}")


class VendorItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = VendorItem

    name = factory.Sequence(lambda n: f"Hot Dog {n}")
    available_on = now()
