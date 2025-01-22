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

        assert response.status_code == 404
        assert response.json() == {"detail": "Radar with this slug not found."}

    def test_missing_slug(self, api_client):
        RadarFactory(label="backend")
        response = api_client.get(reverse("radar-list"))

        assert response.status_code == 404
        assert response.json() == {"detail": "Slug parameter is missing."}
