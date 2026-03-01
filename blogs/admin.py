from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'short_description']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Category', {
            'fields': ('category',)
        }),
        ('Common Fields (Required for all)', {
            'fields': ('image', 'title', 'short_description')
        }),
        ('Property Trends Only', {
            'fields': ('description', 'date', 'time_to_read', 'writer'),
            'classes': ('collapse',),
            'description': 'Fill these only if category is Property Trends'
        }),
        ('Government Schemes Only', {
            'fields': ('link',),
            'classes': ('collapse',),
            'description': 'Fill this only if category is Government Schemes'
        }),
        ('Area Guides Only', {
            'fields': ('lifestyle', 'connectivity', 'key_landmarks', 'avg_price', 'rental_yield'),
            'classes': ('collapse',),
            'description': 'Fill these only if category is Area Guides'
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
