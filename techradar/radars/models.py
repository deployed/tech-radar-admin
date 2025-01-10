from django.db import models
from django_extensions.db.fields import AutoSlugField


class Radar(models.Model):
    label = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from="label")

    def __str__(self):
        return self.slug


## TODO Segment model

## TODO Technology model
