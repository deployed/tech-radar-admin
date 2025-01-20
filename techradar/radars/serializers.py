from rest_framework import serializers
from .models import Radar, Segment, Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"


class SegmentSerializer(serializers.ModelSerializer):
    technology = TechnologySerializer(many=True, source="technology_set")

    class Meta:
        model = Segment
        fields = "__all__"


class RadarSerializer(serializers.ModelSerializer):
    segments = SegmentSerializer(many=True, source="segment_set")

    class Meta:
        model = Radar
        fields = "__all__"
