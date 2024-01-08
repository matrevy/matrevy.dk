from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommonAppConfig(AppConfig):
    name = "matrevy.common"
    verbose_name = _("Fælles")
