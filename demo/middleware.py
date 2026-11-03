import logging
from django.core.exceptions import DisallowedHost

logger = logging.getLogger(__name__)

class LogProxyRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST":
            try:
                django_host = request.get_host()
            except DisallowedHost:
                django_host = "<DisallowedHost>"

            logger.warning(
                "Proxy check: origin=%r host=%r raw_http_host=%r "
                "secure=%r x_forwarded_proto=%r x_forwarded_host=%r remote_addr=%r",
                request.headers.get("Origin"),
                django_host,
                request.META.get("HTTP_HOST"),
                request.is_secure(),
                request.META.get("HTTP_X_FORWARDED_PROTO"),
                request.META.get("HTTP_X_FORWARDED_HOST"),
                request.META.get("REMOTE_ADDR"),
            )

        return self.get_response(request)
