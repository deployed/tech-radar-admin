from rest_framework import viewsets
from .models import Radar
from .serializers import RadarListSerializer, RadarDetailSerializer


class RadarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Radar.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return RadarListSerializer
        if self.action == "retrieve":
            return RadarDetailSerializer
