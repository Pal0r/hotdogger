from django.test import TestCase, Client
from django.urls import get_resolver

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

    def cleanUrl(self, tomodify):
        result = tomodify.replace('(?P<pk>[0-9]+)','1')                
        result = result.replace('(?P<pk>[^/.]+)','1')
        result = result.replace('(?P<employer_id>\d+)','1')
        result = result.replace('$','')
        return result

    def test_get(self):
        
        # Test that only authenticated users have access to secure urls.        
        urls = set(v[1] for k,v in get_resolver(None).reverse_dict.items())
        print('urls:')
        for url in urls:
            if url.startswith('vendor'):
                url = self.cleanUrl(url)                
                redirect_response = self.client.get('/' + url)
                self.assertEqual(redirect_response.status_code, 302)
                print('URL: ' + url)
        
        

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
