from django.contrib import admin
from .models import Radar


@admin.register(Radar)
class RadarAdmin(admin.ModelAdmin):
    list_display = ("label", "slug")
