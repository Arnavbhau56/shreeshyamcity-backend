from django.contrib import admin
from .models import Lead, Enquiry, Agent

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'source', 'status', 'date']
    list_filter = ['status', 'source']
    search_fields = ['name', 'email', 'phone']

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'property', 'status', 'date']
    list_filter = ['status']
    search_fields = ['name', 'property']

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'get_email', 'phone', 'deals']
    search_fields = ['name', 'user__email']
    
    def get_email(self, obj):
        return obj.user.email if obj.user else 'N/A'
    get_email.short_description = 'Email'
