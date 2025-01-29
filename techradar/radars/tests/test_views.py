import pytest
from django.urls import reverse
from techradar.radars.factories import RadarFactory
from rest_framework import status


@pytest.mark.django_db
class TestRadarViewSet:
    def test_get_radar_list(self, api_client):
        RadarFactory(label="Frontend")
        RadarFactory(label="Backend")

        response = api_client.get(reverse("radar-list"))

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [
            {"label": "Frontend", "slug": "frontend"},
            {"label": "Backend", "slug": "backend"},
        ]

    def test_get_proper_radar(self, api_client):
        radar = RadarFactory(label="Backend")

        response = api_client.get(reverse("radar-detail", args=[radar.slug]))

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "label": "Backend",
            "slug": "backend",
            "segments": [],
        }

    def test_slug_not_found(self, api_client):
        RadarFactory(label="Backend")

        response = api_client.get(reverse("radar-detail", args=["frontend"]))

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail": "No Radar matches the given query."}
