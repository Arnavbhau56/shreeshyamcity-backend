from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, EnquiryViewSet, AgentViewSet
from .analytics import analytics_dashboard

router = DefaultRouter()
router.register(r'leads', LeadViewSet, basename='lead')
router.register(r'enquiries', EnquiryViewSet, basename='enquiry')
router.register(r'agents', AgentViewSet, basename='agent')

urlpatterns = [
    path('analytics/dashboard/', analytics_dashboard, name='analytics-dashboard'),
    path('', include(router.urls)),
]
