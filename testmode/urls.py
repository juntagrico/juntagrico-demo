from django.urls import path

from . import views

urlpatterns = [
    path(r'timeout/<int:duration>', views.timeout, name='test-timeout'),
]
