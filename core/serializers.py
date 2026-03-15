from rest_framework import serializers
from .models import Service, Home, Contact, About, Software, Hardware

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Home
        fields=["site_name","tech_name","tagline",
                "availability", "primary_color"]
        
class AboutSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model=About
        fields=["title","content","image"]
    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

class ServiceSerializer(serializers.ModelSerializer):
    is_on_quote=serializers.SerializerMethodField()
    class Meta:
        model=Service
        fields=["id", "name", "description", "price", "is_on_quote", "icon", "order"]
    def get_is_on_quote(self, obj):
        return obj.price is None or obj.price==0
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=["phone","email"]

class SoftwareSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model=Software
        fields=["id", "name", "price", "description", "image", "version", "icon", "order"]

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None

class HardwareSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model=Hardware
        fields=["id", "name", "price", "description", "image", "warranty", "icon", "order"]
    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None