from rest_framework import serializers
from .models import University, ApplicationField

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'location', 'description']
        
class ApplicationFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationField
        fields = [
            'id', 
            'name', 
            'field_type', 
            'is_required',
            'options',
            'allowed_file_types',
            'max_file_size'
            ]
        