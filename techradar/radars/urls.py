from django.urls import path, include
from .views import RadarViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"radar", RadarViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
