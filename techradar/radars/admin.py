from django.contrib import admin
from .models import Radar

class RadarAdmin(admin.ModelAdmin):
    list_display = ('label', 'slug') 

admin.site.register(Radar, RadarAdmin)
