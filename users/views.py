from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import HttpResponse
import csv
from .models import Customer, TeamMember
from .serializers import CustomerSerializer, TeamMemberSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().prefetch_related('properties_bought', 'interested_properties', 'payment_history')
    serializer_class = CustomerSerializer
    
    @action(detail=False, methods=['get'])
    def export_csv(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="customers.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Email', 'Phone', 'Address', 'Status', 'Total Paid', 'Pending Amount', 'Created At'])
        for customer in self.get_queryset():
            writer.writerow([customer.name, customer.email, customer.phone, customer.address, customer.status, customer.total_paid, customer.pending_amount, customer.created_at])
        return response

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
