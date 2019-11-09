from django.test import TestCase

from vendors.tests.factories import VendorFactory


class TestVendor(TestCase):
    def test___str__(self):
        vendor = VendorFactory()
        self.assertEqual(vendor.name, vendor.__str__())
