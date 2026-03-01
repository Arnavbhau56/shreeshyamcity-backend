from django.db import models
from leads.models import Agent

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('Plot', 'Plot'),
        ('Villa', 'Villa'),
        ('Farmhouse', 'Farmhouse'),
        ('Commercial', 'Commercial'),
        ('Apartment', 'Apartment'),
    ]
    
    STATUS_CHOICES = [
        ('Ready to Move', 'Ready to Move'),
        ('Under Construction', 'Under Construction'),
    ]
    
    LISTING_TYPE_CHOICES = [
        ('Buy', 'Buy'),
        ('Rent', 'Rent'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPE_CHOICES)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    area = models.IntegerField()
    dimensions = models.CharField(max_length=50, null=True, blank=True)
    facing = models.CharField(max_length=50, null=True, blank=True)
    amenities = models.JSONField(default=list)
    featured = models.BooleanField(default=False)
    new_launch = models.BooleanField(default=False)
    prime_commercial = models.BooleanField(default=False)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, blank=True, related_name='properties')
    agent_contact = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

class PropertyVideo(models.Model):
    property = models.ForeignKey(Property, related_name='videos', on_delete=models.CASCADE)
    video_url = models.URLField(max_length=500)
    
class Landmark(models.Model):
    CATEGORY_CHOICES = [
        ('Education', 'Education'),
        ('Healthcare', 'Healthcare'),
        ('Transport', 'Transport'),
        ('Lifestyle', 'Lifestyle'),
        ('Religious', 'Religious'),
        ('Business', 'Business'),
    ]
    
    property = models.ForeignKey(Property, related_name='landmarks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    distance = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
