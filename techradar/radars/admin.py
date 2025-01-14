from django.contrib import admin
from .models import Radar, Segment, Technology


class SegmentInline(admin.TabularInline):
    model = Segment
    extra = 0


@admin.register(Radar)
class RadarAdmin(admin.ModelAdmin):
    list_display = ("label", "slug")
    inlines = (SegmentInline,)


class TechnologyInline(admin.StackedInline):
    model = Technology
    extra = 0


@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    list_display = ("label", "slug")
    inlines = (TechnologyInline,)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("label", "slug", "link", "segment", "ring")
