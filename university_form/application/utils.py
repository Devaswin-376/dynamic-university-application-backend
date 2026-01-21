from rest_framework.exceptions import ValidationError
from .models import ApplicationData

# Required field validation
def validate_required_field(field, field_id, data, files):
    if field.is_required and field_id not in data and field_id not in files:
        raise ValidationError(f"'{field.name}' is required.")
    
# File field validation
def validate_file_field(field, uploaded_file):
    #file type validation
    if field.allowed_file_types:
        ext = uploaded_file.name.split('.')[-1].lower()
        if ext not in field.allowed_file_types:
            raise ValidationError(
                f"Invalid file type for '{field.name}'."
                f" Allowed types: {', '.join(field.allowed_file_types)}"
                )
    
    # File size validation
    if field.max_file_size:
        if uploaded_file.size > field.max_file_size * 1024:
            raise ValidationError(
                f"File size for '{field.name}' exceeds the maximum size {field.max_file_size} KB."
            )
         
# Dropdown Field Validation   
def validate_dropdown_field(field, value):
    if field.field_type == 'dropdown' and field.options:
        if value not in field.options:
            raise ValidationError(
                f"Invalid option for '{field.name}'."
                f" Allowed options: {', '.join(field.options)}"
            )
            
# Number Field Validation
def validate_number_field(field, value):
    if field.field_type == 'number':
        try: 
            float(value)
        except ValueError:
            raise ValidationError(f"'{field.name}' must be a valid number.")
        
# Application Data Submit
def save_data(submission, field, value=None, file=None):
    ApplicationData.objects.create(
        submission=submission,
        field=field,
        value=value,
        file=file
    )