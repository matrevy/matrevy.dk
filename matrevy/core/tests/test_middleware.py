# myapp/tests/test_middleware.py
from http import HTTPStatus

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django.test import RequestFactory, SimpleTestCase, override_settings

from ..middleware import RemoveWwwMiddleware


class RemoveWwwMiddlewareTests(SimpleTestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def get_response(self, request):
        return HttpResponse()

    @override_settings(PREPEND_WWW=False)
    def test_www_redirect(self):
        """
        URLs with leading www should get redirected
        """
        request = self.request_factory.get("/", HTTP_HOST="www.example.com")
        response = RemoveWwwMiddleware(self.get_response)(request)
        self.assertEqual(response.status_code, HTTPStatus.MOVED_PERMANENTLY)
        self.assertEqual(response.url, "http://example.com/")

    @override_settings(PREPEND_WWW=False)
    def test_non_redirect(self):
        """
        URLs without leading www should not get redirected
        """
        request = self.request_factory.get("/", HTTP_HOST="example.com")
        response = RemoveWwwMiddleware(self.get_response)(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @override_settings(PREPEND_WWW=True)
    def test_prepend_www_raises(self):
        """
        Middleware incompatible with PREPEND_WWW setting
        """
        msg = (
            "The WWW redirect middleware does not support "
            "the PREPEND_WWW setting."
        )
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            RemoveWwwMiddleware(self.get_response)
