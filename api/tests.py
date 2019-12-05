from rest_framework.test import APITestCase, APIRequestFactory, \
    force_authenticate

from accounts.tests.factories import UserFactory, AuthTokenFactory
from api.views import VendorItemModelViewSet
from vendors.tests.factories import VendorItemFactory, VendorFactory


class TestVendorItemModelViewSet(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.vendor = VendorFactory()
        self.vendor_item = VendorItemFactory(vendor=self.vendor)
        self.user = UserFactory()
        self.vendor.employees.add(self.user)
        self.view = VendorItemModelViewSet.as_view({'get': 'list'})
        self.auth_token = AuthTokenFactory(user=self.user)

    def test_get_queryset(self):
        
        
        request = self.factory.get(f'/api/vendor/{self.vendor.pk}/items/')
        force_authenticate(request, user=self.user, token=self.auth_token.key)
        response = self.view(request, employer_id=self.vendor.pk)

        # Test authenticated request returns correct response
        self.assertEqual(response.status_code, 200)

        # Test response.data for things....
