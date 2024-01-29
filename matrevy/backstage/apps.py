from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BackstageConfig(AppConfig):
    name = "matrevy.backstage"
    verbose_name = _("Backstage")
