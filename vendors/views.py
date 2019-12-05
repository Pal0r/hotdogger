from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.utils import timezone

from vendors.models import VendorItem
from vendors.models import Vendor




class VendorItemListView(LoginRequiredMixin, ListView):
    model = VendorItem
    context_object_name = 'vendor_items'
    
    def get_queryset(self):                
        uservendors = self.request.user.employer.all()
        current_date = datetime.now(tz=timezone.utc)        
        return VendorItem.objects.select_related('vendor').filter(available_on__lte=current_date, vendor__in=uservendors)

class VendorItemUpdateView(LoginRequiredMixin, UpdateView):
    model = VendorItem
    context_object_name = 'hotdog'
    fields = ['name']
    success_url = reverse_lazy('vendor-items')
