from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import User
from leads.models import Agent
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
@permission_classes([AllowAny])
def admin_login(request):
    """Admin/Agent login endpoint"""
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response(
            {'error': 'Email and password are required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        user = User.objects.filter(email=email).first()
        if user and user.check_password(password):
            role = getattr(user, 'role', 'admin')
            
            # Get agent name if user is agent
            agent_name = None
            if role == 'agent':
                agent = Agent.objects.filter(user=user).first()
                if agent:
                    agent_name = agent.name
            
            return Response({
                'success': True,
                'message': 'Login successful',
                'user': {
                    'email': user.email,
                    'username': user.username,
                    'role': role,
                    'agentName': agent_name
                }
            }, status=status.HTTP_200_OK)
    except Exception as e:
        print(f"[LOGIN] Error: {e}")
    
    return Response(
        {'error': 'Invalid credentials'},
        status=status.HTTP_401_UNAUTHORIZED
    )
