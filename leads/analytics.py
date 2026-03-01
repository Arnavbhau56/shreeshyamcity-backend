from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from .models import Lead, Enquiry
from properties.models import Property
from blogs.models import Blog

@api_view(['GET'])
def analytics_dashboard(request):
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    two_weeks_ago = today - timedelta(days=14)
    
    # Current week counts
    properties_count = Property.objects.count()
    leads_count = Lead.objects.count()
    enquiries_count = Enquiry.objects.count()
    blogs_count = Blog.objects.count()
    
    # Previous week counts for growth calculation
    properties_last_week = Property.objects.filter(created_at__lt=week_ago).count()
    leads_last_week = Lead.objects.filter(date__lt=week_ago).count()
    
    # Calculate growth percentages
    properties_growth = calculate_growth(properties_count, properties_last_week)
    leads_growth = calculate_growth(leads_count, leads_last_week)
    
    # Pending enquiries
    pending_enquiries = Enquiry.objects.filter(status='Unread').count()
    
    # Weekly analytics for graphs (last 7 days)
    weekly_data = []
    for i in range(6, -1, -1):
        date = today - timedelta(days=i)
        day_name = date.strftime('%a')
        
        leads_count_day = Lead.objects.filter(date=date).count()
        
        weekly_data.append({
            'name': day_name,
            'leads': leads_count_day,
            'visits': 0  # Placeholder - will be updated by frontend tracking
        })
    
    return Response({
        'stats': {
            'properties': {
                'count': properties_count,
                'growth': properties_growth
            },
            'leads': {
                'count': leads_count,
                'growth': leads_growth
            },
            'enquiries': {
                'count': enquiries_count,
                'pending': pending_enquiries
            },
            'blogs': {
                'count': blogs_count
            }
        },
        'weekly_data': weekly_data
    })

def calculate_growth(current, previous):
    if previous == 0:
        return 100 if current > 0 else 0
    growth = ((current - previous) / previous) * 100
    return round(growth, 1)
