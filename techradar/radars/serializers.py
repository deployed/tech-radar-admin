from rest_framework import serializers
from .models import Radar, Segment, Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["label", "slug", "link", "ring"]


class SegmentSerializer(serializers.ModelSerializer):
    technology = TechnologySerializer(many=True, source="technology_set")

    class Meta:
        model = Segment
        fields = ["label", "slug", "technology", "color"]


class RadarDetailSerializer(serializers.ModelSerializer):
    segments = SegmentSerializer(many=True, source="segment_set")

    class Meta:
        model = Radar
        fields = ["label", "slug", "segments"]


class RadarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radar
        fields = ["label", "slug", "color"]
