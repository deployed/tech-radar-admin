from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField


class Radar(models.Model):
    label = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from="label")

    def __str__(self):
        return self.slug


class Segment(models.Model):
    label = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from="label")
    radar = models.ForeignKey(Radar, on_delete=models.CASCADE, default=None)
    color = ColorField(default="#FF0000")

    def __str__(self):
        return f"{self.slug} [{self.radar.slug}]"


class Ring(models.TextChoices):
    ADOPT = "adopt", _("adopt")
    HOLD = "hold", _("hold")
    ASSESS = "assess", _("assess")
    TRIAL = "trial", _("trial")


class Technology(models.Model):
    label = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="label")
    link = models.URLField(max_length=150)
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, default=None)
    ring = models.CharField(max_length=7, choices=Ring.choices, default=Ring.ADOPT)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologies")
