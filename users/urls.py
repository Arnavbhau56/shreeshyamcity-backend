from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, TeamMemberViewSet
from .admin_views import admin_login

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'team', TeamMemberViewSet, basename='team')

urlpatterns = [
    path('admin/login/', admin_login, name='admin-login'),
    path('', include(router.urls)),
]
