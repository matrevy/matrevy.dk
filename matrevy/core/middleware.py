from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponsePermanentRedirect


class RemoveWwwMiddleware:
    """
    Middleware that removes www from incoming requests.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        if getattr(settings, "PREPEND_WWW", None):
            raise ImproperlyConfigured(
                "The remove WWW middleware does not support "
                "the PREPEND_WWW setting."
            )

    def __call__(self, request):
        host = request.get_host()
        if host and host.startswith("www."):
            redirect_host = host.removeprefix("www.")
            path = request.get_full_path()
            return HttpResponsePermanentRedirect(
                f"{request.scheme}://{redirect_host}{path}"
            )
        return self.get_response(request)
