from django.contrib import admin
from .models import Property, PropertyImage, PropertyVideo, Landmark

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

class PropertyVideoInline(admin.TabularInline):
    model = PropertyVideo
    extra = 1

class LandmarkInline(admin.TabularInline):
    model = Landmark
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'location', 'price', 'status', 'agent', 'featured', 'created_at']
    list_filter = ['type', 'status', 'listing_type', 'featured', 'new_launch', 'prime_commercial', 'agent']
    search_fields = ['title', 'location', 'description']
    inlines = [PropertyImageInline, PropertyVideoInline, LandmarkInline]
