from rest_framework import serializers
from .models import User, Customer, PropertyBought, InterestedProperty, PaymentHistory, TeamMember

class PropertyBoughtSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyBought
        fields = ['id', 'property_id', 'title', 'price', 'date']

class InterestedPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestedProperty
        fields = ['id', 'property_id', 'title', 'status']

class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = ['id', 'amount', 'date', 'description', 'status']

class CustomerSerializer(serializers.ModelSerializer):
    properties_bought = PropertyBoughtSerializer(many=True, required=False)
    interested_properties = InterestedPropertySerializer(many=True, required=False)
    payment_history = PaymentHistorySerializer(many=True, required=False)
    
    class Meta:
        model = Customer
        fields = '__all__'
    
    def create(self, validated_data):
        properties_bought_data = validated_data.pop('properties_bought', [])
        interested_properties_data = validated_data.pop('interested_properties', [])
        payment_history_data = validated_data.pop('payment_history', [])
        
        customer = Customer.objects.create(**validated_data)
        
        for prop_data in properties_bought_data:
            PropertyBought.objects.create(customer=customer, **prop_data)
        for prop_data in interested_properties_data:
            InterestedProperty.objects.create(customer=customer, **prop_data)
        for pay_data in payment_history_data:
            PaymentHistory.objects.create(customer=customer, **pay_data)
        
        return customer
    
    def update(self, instance, validated_data):
        properties_bought_data = validated_data.pop('properties_bought', None)
        interested_properties_data = validated_data.pop('interested_properties', None)
        payment_history_data = validated_data.pop('payment_history', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if properties_bought_data is not None:
            instance.properties_bought.all().delete()
            for prop_data in properties_bought_data:
                PropertyBought.objects.create(customer=instance, **prop_data)
        
        if interested_properties_data is not None:
            instance.interested_properties.all().delete()
            for prop_data in interested_properties_data:
                InterestedProperty.objects.create(customer=instance, **prop_data)
        
        if payment_history_data is not None:
            instance.payment_history.all().delete()
            for pay_data in payment_history_data:
                PaymentHistory.objects.create(customer=instance, **pay_data)
        
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'first_name', 'last_name']

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'
