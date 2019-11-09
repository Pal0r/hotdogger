from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied

from api.serializers import VendorItemSerializer
from vendors.models import VendorItem, Vendor


class VendorItemModelViewSet(ModelViewSet):
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
