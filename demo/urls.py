from django.conf import settings
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'impersonate/', include('impersonate.urls')),
    path('',include('juntagrico_billing.urls')),
    path(r'', include('juntagrico.urls')),
]

# Test mode
if settings.TEST_MODE:
    urlpatterns.append(
        path('test/', include('testmode.urls')),
    )
