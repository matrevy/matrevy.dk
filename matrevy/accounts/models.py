from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Account(AbstractUser):
    class Type(models.TextChoices):
        INDIVIDUAL = "INDIVIDUAL", _("Individuel")
        REVUE = "REVUE", _("Revy")

    type = models.CharField(
        _("Type"),
        max_length=30,
        choices=Type.choices,
        default=Type.INDIVIDUAL,
    )
    created = models.DateTimeField(_("oprettet"), auto_now_add=True)
    modified = models.DateTimeField(_("ændret"), auto_now=True)

    class Meta:
        verbose_name = _("konto")
        verbose_name_plural = _("konti")
