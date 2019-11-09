from rest_framework import routers

from api.views import VendorItemModelViewSet

router = routers.DefaultRouter()

router.register(r'vendor/(?P<employer_id>\d+)/items', VendorItemModelViewSet)

urlpatterns = router.urls
