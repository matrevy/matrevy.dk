import os

from django.db import models
from django.utils.translation import gettext_lazy as _

from django_hosts.resolvers import reverse


def upload_poster_path(instance, filename):
    _, ext = os.path.splitext(filename)
    filename = instance.slug + ext
    return f"revues/posters/{filename}"


class Revue(models.Model):
    """
    TODO
    """

    slug = models.SlugField(_("URL-slug"), unique=True)
    title = models.CharField(_("titel"), max_length=200)
    description = models.TextField(_("beskrivelse"), blank=True)
    opening_date = models.DateField(_("premierdato"))
    # closing_date = models.DateField(_("slutdato"))
    poster = models.ImageField(
        _("plakat"),
        upload_to=upload_poster_path,
        blank=True,
    )

    objects = models.Manager()

    class Meta:
        verbose_name = _("revy")
        verbose_name_plural = _("revyer")
        ordering = ["-opening_date"]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        kwargs = {
            "slug": self.slug,
        }
        return reverse("revues:detail", host="matrevy", kwargs=kwargs)

    @property
    def year(self):
        return self.opening_date.year


class Scene(models.Model):
    """
    Model for scenes
    """

    class SceneType(models.TextChoices):
        SKETCH = "SKETCH", _("Sketch")
        SONG = "SONG", _("Song")
        VIDEO = "VIDEO", _("Video")
        # DANCE = "DANCE", _("Dans")
        # INTERLUDE = "INTERLUDE", _("Pausefisk")
        # MEDLEY = "MEDLEY", _("Medley")

    title = models.CharField(_("titel"), max_length=200)
    type = models.CharField(_("type"), max_length=20, choices=SceneType.choices, default=SceneType.SKETCH)
    duration = models.IntegerField(_("varighed"), blank=True, null=True)
    # author = models.CharField(_("forfatter"), max_length=100)
    revue = models.ForeignKey(Revue, on_delete=models.CASCADE)
    act_no = models.PositiveIntegerField()
    scene_no = models.PositiveIntegerField()

    class Meta:
        verbose_name = _("scene")
        verbose_name_plural = _("scener")
        ordering = ["-revue", "act_no", "scene_no"]

    def __str__(self):
        return self.title

