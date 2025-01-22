from django_filters import rest_framework as filters
from .models import Radar


class RadarFilter(filters.FilterSet):
    slug = filters.CharFilter(lookup_expr="exact")

    class Meta:
        model = Radar
        fields = ["slug"]
