from rest_framework import serializers
from .models import Property, PropertyImage, PropertyVideo, Landmark
from leads.serializers import AgentSerializer

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['id', 'image_url', 'order']

class PropertyVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyVideo
        fields = ['id', 'video_url']

class LandmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landmark
        fields = ['id', 'name', 'distance', 'category']

class PropertySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    videos = serializers.SerializerMethodField()
    landmarks = LandmarkSerializer(many=True, read_only=True)
    coordinates = serializers.SerializerMethodField()
    agent_details = AgentSerializer(source='agent', read_only=True)
    
    class Meta:
        model = Property
        fields = '__all__'
    
    def get_images(self, obj):
        return [img.image_url for img in obj.images.all()]
    
    def get_videos(self, obj):
        return [vid.video_url for vid in obj.videos.all()]
    
    def get_coordinates(self, obj):
        if obj.latitude and obj.longitude:
            return {'lat': float(obj.latitude), 'lng': float(obj.longitude)}
        return None

class PropertyCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.DictField(),
        write_only=True,
        required=False
    )
    videos = serializers.ListField(
        child=serializers.DictField(),
        write_only=True,
        required=False
    )
    landmarks = LandmarkSerializer(many=True, write_only=True, required=False)
    
    class Meta:
        model = Property
        fields = '__all__'
    
    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        videos_data = validated_data.pop('videos', [])
        landmarks_data = validated_data.pop('landmarks', [])
        
        property_obj = Property.objects.create(**validated_data)
        
        # Handle images - can be dict with image_url or just string
        for idx, img_data in enumerate(images_data):
            img_url = img_data.get('image_url') if isinstance(img_data, dict) else img_data
            order = img_data.get('order', idx) if isinstance(img_data, dict) else idx
            PropertyImage.objects.create(property=property_obj, image_url=img_url, order=order)
        
        # Handle videos - can be dict with video_url or just string
        for vid_data in videos_data:
            vid_url = vid_data.get('video_url') if isinstance(vid_data, dict) else vid_data
            PropertyVideo.objects.create(property=property_obj, video_url=vid_url)
        
        for landmark_data in landmarks_data:
            Landmark.objects.create(property=property_obj, **landmark_data)
        
        return property_obj
    
    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', None)
        videos_data = validated_data.pop('videos', None)
        landmarks_data = validated_data.pop('landmarks', None)
        
        # Update basic fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Update images if provided
        if images_data is not None:
            instance.images.all().delete()
            for idx, img_data in enumerate(images_data):
                img_url = img_data.get('image_url') if isinstance(img_data, dict) else img_data
                order = img_data.get('order', idx) if isinstance(img_data, dict) else idx
                PropertyImage.objects.create(property=instance, image_url=img_url, order=order)
        
        # Update videos if provided
        if videos_data is not None:
            instance.videos.all().delete()
            for vid_data in videos_data:
                vid_url = vid_data.get('video_url') if isinstance(vid_data, dict) else vid_data
                PropertyVideo.objects.create(property=instance, video_url=vid_url)
        
        # Update landmarks if provided
        if landmarks_data is not None:
            instance.landmarks.all().delete()
            for landmark_data in landmarks_data:
                Landmark.objects.create(property=instance, **landmark_data)
        
        return instance
