from django.db import models

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('property_trends', 'Property Trends in Dhanbad'),
        ('government_schemes', 'Government Housing Schemes'),
        ('area_guides', 'Area Guides'),
    ]
    
    # Common fields (1-4)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.URLField(max_length=500)
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    
    # Field 5: Only for Property Trends
    description = models.TextField(blank=True, null=True)
    
    # Field 6: Only for Government Housing Schemes
    link = models.URLField(max_length=500, blank=True, null=True)
    
    # Fields 7-11: Only for Area Guides
    lifestyle = models.TextField(blank=True, null=True)
    connectivity = models.TextField(blank=True, null=True)
    key_landmarks = models.JSONField(blank=True, null=True)
    avg_price = models.CharField(max_length=100, blank=True, null=True)
    rental_yield = models.CharField(max_length=50, blank=True, null=True)
    
    # Fields 12-14: Only for Property Trends
    date = models.DateField(blank=True, null=True)
    time_to_read = models.CharField(max_length=50, blank=True, null=True)
    writer = models.CharField(max_length=100, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_category_display()} - {self.title}"
