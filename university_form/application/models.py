from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=255,null=False)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
class ApplicationField(models.Model):
    FIELDS_TYPES = [
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('dropdown', 'Dropdown'),
        ('file', 'File'),
    ]
    
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='fields')
    name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20, choices=FIELDS_TYPES)
    is_required = models.BooleanField(default=False)
    
    options = models.JSONField(blank= True, null=True)
    allowed_file_types = models.JSONField(blank= True, null=True)
    max_file_size = models.IntegerField(blank= True, null=True) # in KB
    
    def __str__(self):
        return f"{self.name} ({self.university.name})"
    
class ApplicationSubmission(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    
class ApplicationData(models.Model):
    submission = models.ForeignKey(ApplicationSubmission, on_delete=models.CASCADE)
    field = models.ForeignKey(ApplicationField, on_delete=models.CASCADE)
    value = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='applications/', blank=True, null=True)