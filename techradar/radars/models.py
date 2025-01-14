from django.db import models
from django_extensions.db.fields import AutoSlugField


class Radar(models.Model):
    label = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from="label")

    def __str__(self):
        return self.slug


class Segment(models.Model):
    label = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from="label")
    radar = models.ForeignKey(Radar, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.slug} [{self.radar.slug}]"


class Ring(models.TextChoices):
    ADOPT = "adopt"
    HOLD = "hold"
    ASSESS = "assess"
    TRIAL = "trial"


class Technology(models.Model):
    label = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from="label")
    link = models.CharField(max_length=100)
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, default=None)
    ring = models.CharField(max_length=7, choices=Ring.choices, default=Ring.ADOPT)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
