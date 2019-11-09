from django.contrib import admin

from vendors.models import Vendor, VendorItem


admin.site.register(Vendor)
admin.site.register(VendorItem)