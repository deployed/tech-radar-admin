from django.contrib import admin
from .models import Radar, Segment, Technology


@admin.register(Radar)
class RadarAdmin(admin.ModelAdmin):
    list_display = ("label", "slug")


@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    list_display = ("label", "slug")


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("label", "slug", "link", "segment", "ring")
