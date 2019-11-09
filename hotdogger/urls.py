from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Hotdogger API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('core.urls')),
    path('vendors/', include('vendors.urls')),
    path('api/', include('api.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('api-docs/', schema_view),
        path('__debug__/', include(debug_toolbar.urls)),
    ]
