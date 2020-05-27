from django.apps import AppConfig

_ = gettext_lazy = lambda s: s


class CoreConfig(AppConfig):
    name = 'matrevy.core'
    verbose_name = _('Core')
