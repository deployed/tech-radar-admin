from rest_framework.exceptions import NotFound
from rest_framework import viewsets
from .models import Radar
from .serializers import RadarSerializer


class RadarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Radar.objects.all()
    serializer_class = RadarSerializer

    def get_queryset(self):
        slug = self.request.query_params.get("slug", None)
        if slug:
            queryset = self.queryset.filter(slug=slug)
            if not queryset.exists():
                raise NotFound(detail="Radar with this slug not found.")
            return queryset
        else:
            raise NotFound(detail="Slug parameter is missing.")
