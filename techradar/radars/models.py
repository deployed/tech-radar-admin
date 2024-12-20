from django.db import models


class Radar(models.Model):
    label = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug
    

## TODO Segment model

## TODO Technology model