from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Customer, PropertyBought, InterestedProperty, PaymentHistory, TeamMember

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'role', 'agent_profile')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff']
    list_filter = ['role', 'is_staff', 'is_superuser']

admin.site.register(User, UserAdmin)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'email', 'phone', 'experience', 'order']
    list_editable = ['order']
    search_fields = ['name', 'role', 'email']
    ordering = ['order']

class PropertyBoughtInline(admin.TabularInline):
    model = PropertyBought
    extra = 0

class InterestedPropertyInline(admin.TabularInline):
    model = InterestedProperty
    extra = 0

class PaymentHistoryInline(admin.TabularInline):
    model = PaymentHistory
    extra = 0

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'status', 'total_paid', 'pending_amount']
    list_filter = ['status']
    search_fields = ['name', 'email', 'phone']
    inlines = [PropertyBoughtInline, InterestedPropertyInline, PaymentHistoryInline]
