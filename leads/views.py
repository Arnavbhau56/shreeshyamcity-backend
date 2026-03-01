from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password, check_password
from .models import Lead, Enquiry, Agent
from .serializers import LeadSerializer, EnquirySerializer, AgentSerializer
from .mailing import send_enquiry_confirmation, send_lead_notification
from users.models import User

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all().order_by('-date')
    serializer_class = LeadSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        agent_id = self.request.query_params.get('agent_id')
        if agent_id:
            queryset = queryset.filter(assigned_agent_id=agent_id)
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Send email asynchronously (don't block response)
        lead_data = serializer.data
        try:
            send_lead_notification(
                lead_data.get('name'),
                lead_data.get('email'),
                lead_data.get('phone'),
                lead_data.get('message', '')
            )
        except Exception as e:
            print(f"Email failed but lead saved: {e}")
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = Enquiry.objects.all().order_by('-date')
    serializer_class = EnquirySerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Send email asynchronously (don't block response)
        enquiry_data = serializer.data
        try:
            send_enquiry_confirmation(
                enquiry_data.get('name'),
                request.data.get('email', ''),
                enquiry_data.get('property')
            )
        except Exception as e:
            print(f"Email failed but enquiry saved: {e}")
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        
        # Validate required fields
        if not data.get('name') or not data.get('role'):
            return Response({'error': 'Name and role are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create User account for agent if email and password provided
        if data.get('email') and data.get('password'):
            # Use first name as username
            username = data.get('name', '').split()[0].lower()
            
            # Make username unique if already exists
            base_username = username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            
            # Check if email already exists
            if User.objects.filter(email=data['email']).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                user = User.objects.create_user(
                    username=username,
                    email=data['email'],
                    password=data['password'],
                    role='agent'
                )
                
                # Create agent with user reference
                agent = Agent.objects.create(
                    user=user,
                    name=data.get('name'),
                    role=data.get('role'),
                    phone=data.get('phone', ''),
                    photo=data.get('photo', ''),
                    deals=int(data.get('deals', 0))
                )
                
                serializer = self.get_serializer(agent)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Create agent without user account
            try:
                agent = Agent.objects.create(
                    name=data.get('name'),
                    role=data.get('role'),
                    phone=data.get('phone', ''),
                    photo=data.get('photo', ''),
                    deals=int(data.get('deals', 0))
                )
                serializer = self.get_serializer(agent)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        # Add email from user if available
        data = serializer.data
        for item in data:
            agent = Agent.objects.get(id=item['id'])
            if agent.user:
                item['email'] = agent.user.email
            else:
                item['email'] = ''
        
        return Response({'results': data})
    
    @action(detail=False, methods=['get'])
    def export_csv(self, request):
        import csv
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="agents.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Role', 'Email', 'Phone', 'Deals'])
        
        for agent in self.get_queryset():
            email = agent.user.email if agent.user else ''
            writer.writerow([agent.name, agent.role, email, agent.phone, agent.deals])
        
        return response
