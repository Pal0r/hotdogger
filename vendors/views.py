from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy

from vendors.models import VendorItem


class VendorItemListView(ListView):
    model = VendorItem
    context_object_name = 'vendor_items'


class VendorItemUpdateView(UpdateView):
    model = VendorItem
    context_object_name = 'hotdog'
    fields = ['name']
    success_url = reverse_lazy('vendor-items')
