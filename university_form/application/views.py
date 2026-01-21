from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from .models import University, ApplicationField, ApplicationSubmission, ApplicationData
from .serializers import UniversitySerializer, ApplicationFieldSerializer
from .utils import (
    validate_required_field,
    validate_file_field,
    validate_dropdown_field,
    validate_number_field,
    save_data
)
# Create your views here.

class UniversityListAPIView(APIView):
    def get(self, request):
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)
    
class UniversityDetailAPIView(APIView):
    def get(self, request, university_id):
        university = get_object_or_404(University, id=university_id)
        serializer = UniversitySerializer(university)
        return Response(serializer.data)
    
class ApplicationFieldsAPIView(APIView):
    def get(self, request, university_id):
        university = get_object_or_404(University, id=university_id)
        fields = ApplicationField.objects.filter(university=university).order_by('id')  
        serializer = ApplicationFieldSerializer(fields, many=True)
        return Response(serializer.data)
    
class SubmitApplicationAPIView(APIView):
    def post(self, request):
        university_id = request.data.get('university_id')
        university = get_object_or_404(University, id=university_id)
        submission = ApplicationSubmission.objects.create(university=university)
        fields = ApplicationField.objects.filter(university=university)

        try :     
            for field in fields:
                field_id = f"field_{field.id}"

                validate_required_field(field, field_id, request.data, request.FILES)
                
                if field.field_type == 'file' and field_id in request.FILES:
                    uploaded_file = request.FILES[field_id]
                    validate_file_field(field, uploaded_file)
                    save_data(submission, field, file=uploaded_file)
            
                elif field_id in request.data:
                    value = request.data.get(field_id)
                    validate_dropdown_field(field, value)
                    validate_number_field(field, value)
                    save_data(submission, field, value=value)
                    
            return Response(
            {"message": "Application submitted successfully."},
                    status=status.HTTP_201_CREATED
                )  
            
        except ValidationError as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            ) 
                


