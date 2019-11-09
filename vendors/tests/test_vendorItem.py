from django.test import TestCase, Client

from django.contrib.auth.models import User
from vendors.models import VendorItem, Vendor
from django.utils.timezone import now


class TestVendorItemTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create(username='test1', password='bingo123456', is_active=True)

    def test_get(self):
        vendor = Vendor.objects.create(name='test vendor')
        vendor_item = VendorItem.objects.create(name='hotdog', vendor=vendor, available_on=now())

        redirect_response = self.client.get('/vendors/items/')
        # Test that only authenticated users can view this page.
        self.assertEqual(redirect_response.status_code, 302)

        # Test that logged in users can view the vendor item list page
        self.client.force_login(self.user)
        response = self.client.get('/vendors/items/')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context['object_list'][0].name, vendor_item.name)

