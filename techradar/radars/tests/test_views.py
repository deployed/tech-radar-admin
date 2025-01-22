import pytest
from django.urls import reverse
from techradar.radars.factories import RadarFactory


@pytest.mark.django_db
class TestRadarViewSet:
    def test_get_proper_radar(self, api_client):
        RadarFactory(label="backend")
        response = api_client.get(reverse("radar-list"), {"slug": "backend"})

        assert response.status_code == 200
        assert response.json() == [
            {"label": "backend", "slug": "backend", "segments": []}
        ]

    def test_slug_not_found(self, api_client):
        RadarFactory(label="backend")
        response = api_client.get(reverse("radar-list"), {"slug": "frontend"})

        assert response.status_code == 200
        assert response.json() == []
