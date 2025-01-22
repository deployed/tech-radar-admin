from rest_framework import viewsets
from .models import Radar
from .serializers import RadarSerializer
from django_filters import rest_framework as filters
from .filters import RadarFilter


class RadarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Radar.objects.all()
    serializer_class = RadarSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RadarFilter
