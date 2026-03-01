from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('agent', 'Agent'),
    ]
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='admin')
    agent_profile = models.OneToOneField('leads.Agent', on_delete=models.SET_NULL, null=True, blank=True, related_name='user_account')

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.URLField(max_length=500)
    bio = models.TextField()
    specialization = models.JSONField(default=list)
    experience = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    languages = models.JSONField(default=list)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('VIP', 'VIP'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    avatar_url = models.URLField(max_length=500, null=True, blank=True)
    total_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    pending_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class PropertyBought(models.Model):
    customer = models.ForeignKey(Customer, related_name='properties_bought', on_delete=models.CASCADE)
    property_id = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()

class InterestedProperty(models.Model):
    STATUS_CHOICES = [
        ('Viewed', 'Viewed'),
        ('Contacted', 'Contacted'),
        ('Offer Made', 'Offer Made'),
    ]
    
    customer = models.ForeignKey(Customer, related_name='interested_properties', on_delete=models.CASCADE)
    property_id = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class PaymentHistory(models.Model):
    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
    ]
    
    customer = models.ForeignKey(Customer, related_name='payment_history', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
