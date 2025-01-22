import factory.fuzzy
from factory.django import DjangoModelFactory
from .models import Radar, Segment, Technology


class RadarFactory(DjangoModelFactory):
    label = factory.Faker("word")

    class Meta:
        model = Radar


class SegmentFactory(DjangoModelFactory):
    label = factory.Faker("word")
    radar = factory.SubFactory(RadarFactory)

    class Meta:
        model = Segment


class TechnologyFactory(DjangoModelFactory):
    label = factory.Faker("word")
    segment = factory.SubFactory(SegmentFactory)

    class Meta:
        model = Technology
