from rest_framework.serializers import ModelSerializer

from vendors.models import VendorItem


class VendorItemSerializer(ModelSerializer):
    class Meta:
        model = VendorItem
        fields = '__all__'
