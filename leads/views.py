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
        
        # Create User account for agent if email provided
        if 'email' in data and 'password' in data:
            # Use first name as username
            username = data.get('name', '').split()[0].lower()
            
            # Make username unique if already exists
            if User.objects.filter(username=username).exists():
                username = f"{username}{User.objects.filter(username__startswith=username).count() + 1}"
            
            # Check if email already exists
            if User.objects.filter(email=data['email']).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = User.objects.create_user(
                username=username,
                email=data['email'],
                password=data['password'],
                role='agent'
            )
            agent_data = {
                'user': user.id,
                'name': data.get('name'),
                'role': data.get('role'),
                'phone': data.get('phone', ''),
                'photo': data.get('photo', ''),
                'deals': data.get('deals', 0)
            }
        else:
            # Create agent without user account
            agent_data = {
                'name': data.get('name'),
                'role': data.get('role'),
                'phone': data.get('phone', ''),
                'photo': data.get('photo', ''),
                'deals': data.get('deals', 0)
            }
        
        serializer = self.get_serializer(data=agent_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            agent = Agent.objects.get(email=email)
            if check_password(password, agent.password):
                serializer = self.get_serializer(agent)
                return Response(serializer.data)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Agent.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
