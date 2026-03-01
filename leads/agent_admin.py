from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from .models import Lead
import csv
from django.http import HttpResponse

class AgentAdminSite(AdminSite):
    site_header = _('Agent Dashboard')
    site_title = _('Agent Portal')
    index_title = _('My Leads')

agent_admin_site = AgentAdminSite(name='agent_admin')

def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=my_leads.csv'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Phone', 'Message', 'Source', 'Status', 'Date'])
    for lead in queryset:
        writer.writerow([lead.name, lead.email, lead.phone, lead.message, lead.source, lead.status, lead.date])
    return response
export_to_csv.short_description = "Export to CSV"

class AgentLeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'source', 'status', 'date']
    list_filter = ['status', 'source']
    search_fields = ['name', 'email', 'phone']
    actions = [export_to_csv]
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role == 'agent' and request.user.agent_profile:
            return qs.filter(agent=request.user.agent_profile)
        return qs
    
    def save_model(self, request, obj, form, change):
        if request.user.role == 'agent' and request.user.agent_profile:
            obj.agent = request.user.agent_profile
            obj.source = request.user.agent_profile.name
        super().save_model(request, obj, form, change)
    
    def has_module_permission(self, request):
        return request.user.role == 'agent'

agent_admin_site.register(Lead, AgentLeadAdmin)
