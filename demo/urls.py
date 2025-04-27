from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'impersonate/', include('impersonate.urls')),
    path('',include('juntagrico_billing.urls')),
    path(r'', include('juntagrico.urls')),
]
