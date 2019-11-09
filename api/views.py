from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied

from api.serializers import VendorItemSerializer
from vendors.models import VendorItem, Vendor


class VendorItemModelViewSet(ModelViewSet):
    queryset = VendorItem.objects.all()
    serializer_class = VendorItemSerializer
