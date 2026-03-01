from rest_framework import serializers
from .models import Lead, Enquiry, Agent

class AgentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = Agent
        fields = ['id', 'name', 'role', 'phone', 'deals', 'photo', 'email', 'password', 'user']
        read_only_fields = ['user']

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = ['id', 'name', 'email', 'phone', 'property', 'message', 'date', 'status']
