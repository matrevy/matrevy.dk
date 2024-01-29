from django.conf import settings

from django_hosts import host, patterns


host_patterns = patterns("",
    host("", settings.ROOT_URLCONF, name="matrevy"),
    host("admin", "config.urls.admin", name="admin"),
    host("backstage", "config.urls.backstage", name="backstage"),
)
