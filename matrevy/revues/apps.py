from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RevuesConfig(AppConfig):
    name = "matrevy.revues"
    verbose_name = _("Revyer")
