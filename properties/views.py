from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Property
from .serializers import PropertySerializer, PropertyCreateSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().prefetch_related('images', 'videos', 'landmarks').order_by('-created_at')
    serializer_class = PropertySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['price', 'created_at', 'area']
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PropertyCreateSerializer
        return PropertySerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Manual filtering
        property_type = self.request.query_params.get('type')
        status = self.request.query_params.get('status')
        listing_type = self.request.query_params.get('listing_type')
        location = self.request.query_params.get('location')
        featured = self.request.query_params.get('featured')
        
        if property_type:
            queryset = queryset.filter(type=property_type)
        if status:
            queryset = queryset.filter(status=status)
        if listing_type:
            queryset = queryset.filter(listing_type=listing_type)
        if location:
            queryset = queryset.filter(location=location)
        if featured:
            queryset = queryset.filter(featured=featured.lower() == 'true')
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_properties = self.queryset.filter(featured=True)
        serializer = self.get_serializer(featured_properties, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def new_launches(self, request):
        new_properties = self.queryset.filter(new_launch=True)
        serializer = self.get_serializer(new_properties, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def commercial(self, request):
        commercial_properties = self.queryset.filter(prime_commercial=True)
        serializer = self.get_serializer(commercial_properties, many=True)
        return Response(serializer.data)
