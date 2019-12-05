from django.test import TestCase, Client

from accounts.tests.factories import UserFactory
from vendors.tests.factories import VendorFactory, VendorItemFactory


class TestVendorItemTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserFactory()
        self.vendor = VendorFactory()
        self.vendor.employees.add(self.user)
        self.vendor_item = VendorItemFactory(vendor=self.vendor)

    def test___str__(self):
        vendoritem = VendorItemFactory(vendor=self.vendor)
        self.assertEqual(vendoritem.name, vendoritem.__str__())

    def test_get(self):
        redirect_response = self.client.get('/vendors/items/')
        # Test that only authenticated users can view this page.
        self.assertEqual(redirect_response.status_code, 302)

        # Test that logged in users can view the vendor item list page
        self.client.force_login(self.user)
        response = self.client.get('/vendors/items/')
        self.assertEqual(response.status_code, 200)

        # Test view response context contains created vendor item.
        self.assertEqual(
            response.context['object_list'][0].name,
            self.vendor_item.name
        )

        # Test vendor items in response are within the availability window.

        # Test response does not contain another vendor's items.
