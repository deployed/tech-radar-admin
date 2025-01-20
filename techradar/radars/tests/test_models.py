import pytest
from techradar.radars.factories import TechnologyFactory, RadarFactory, SegmentFactory


@pytest.mark.django_db
class TestRadarViewSet:
    def test_radar_factory(self):
        radar = RadarFactory()

        assert radar.slug is not None

    def test_segment_factory(self):
        segment = SegmentFactory()

        assert segment.slug is not None
        assert segment.radar is not None

    def test_technology_factory(self):
        technology = TechnologyFactory()

        assert technology.slug is not None
        assert technology.segment is not None
