from django.urls import path

from vendors.views import VendorItemListView, VendorItemUpdateView

urlpatterns = [
    path('items/', VendorItemListView.as_view(), name='vendor-items'),
    path('items/<int:pk>/', VendorItemUpdateView.as_view(), name='update-vendor-item'),
]
