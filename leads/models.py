from django.db import models

class Lead(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Closed', 'Closed'),
    ]
    
    SOURCE_CHOICES = [
        ('Website', 'Website'),
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('Referral', 'Referral'),
        ('Other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    property_id = models.CharField(max_length=50, null=True, blank=True)
    source = models.CharField(max_length=100, default='Website')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    assigned_agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True, blank=True, related_name='leads')
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.status}"

class Enquiry(models.Model):
    STATUS_CHOICES = [
        ('Unread', 'Unread'),
        ('Read', 'Read'),
        ('Resolved', 'Resolved'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    property = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Unread')
    
    def __str__(self):
        return f"{self.name} - {self.property}"

class Agent(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='agent_info', null=True, blank=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    deals = models.IntegerField(default=0)
    photo = models.URLField(max_length=500, null=True, blank=True)
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.name
