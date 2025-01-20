import factory.fuzzy
from factory.django import DjangoModelFactory
from faker import Faker
from .models import Radar, Segment, Technology

fake = Faker()


class RadarFactory(DjangoModelFactory):
    label = factory.LazyFunction(fake.word)

    class Meta:
        model = Radar


class SegmentFactory(DjangoModelFactory):
    label = factory.LazyFunction(fake.word)
    radar = factory.SubFactory(RadarFactory)

    class Meta:
        model = Segment


class TechnologyFactory(DjangoModelFactory):
    label = factory.LazyFunction(fake.word)
    segment = factory.SubFactory(SegmentFactory)

    class Meta:
        model = Technology
