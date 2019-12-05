from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin


from api.serializers import VendorItemSerializer
from vendors.models import VendorItem, Vendor


class VendorItemModelViewSet(LoginRequiredMixin,ModelViewSet):
    """
    retrieve:
        Returns a given Vendor Item/Hotdog.

    list:
        Return a list of all hotdogs for a given vendor.

    create:
        description missing.

    destroy:
        description missing.

    update:
        description missing.

    partial_update:
        description missing.
    """
    queryset = VendorItem.objects.all()
    serializer_class = VendorItemSerializer

    def get_queryset(self):
        requested_vendor = self.request.parser_context['kwargs']['employer_id']         
        return self.queryset.filter(vendor_id=requested_vendor)